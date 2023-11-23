import streamlit as st
from data.const import *
from data.sendData import *
from components.custom import *
from data.getItemDetail import get_data_index


def get_inputs(data, nomor_po, index=0, source="Manual"):
    #=============================================#
    #----------------- VAR INIT ------------------#
    #=============================================#
    if source == "Manual":
        id, date_val, material_val, tender_val, item, ka_val, rkap_val, tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val, vendor_val, status_val, deliv_val, penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, other2_val, file_loc_val, forecast_val, cumulative_val, ir_val, a_val = get_data_index(data, index)

    #=============================================#
    #------------------- DATA --------------------#
    #=============================================#
    with st.spinner("Loading Data"):
        st.divider()
        st.header("DATA")

        item_name = st.text_input("Item", item, placeholder="Item Name")

        col1, col2 = st.columns([1, 2])
        with col1: 
            selected_date = st.date_input("PR Month", date_val)
        with col2:        
            material_service = st.selectbox("Material/Service", material_options, index=tuple(material_options["M"]).index(material_val))

        col1, col2, col3 = st.columns(3)
        with col1:
            ka = st.selectbox("K/A", ka_option, index=tuple(ka_option["M"]).index(ka_val))
        with col2:
            rkap = st.number_input("RKAP", value=rkap_val)
        with col3:
            tpn = st.selectbox("TA/Punchlist/Normal", tpn_option, index=tuple(tpn_option["M"]).index(tpn_val))

        col1, col2 = st.columns([2,1])
        with col1: 
            coa = st.selectbox("COA", coa_option, index=tuple(coa_option["M"]).index(coa_val))
        with col2:
            discipline = st.selectbox("Discipline", discipline_option, index=tuple(discipline_option["M"]).index(discipline_val))

        col1, col2, col3 = st.columns(3)
        with col1:
            eproc = st.selectbox("E-Proc/PaDi/Normal", eproc_option, index=tuple(eproc_option["M"]).index(eproc_val))
        with col2:
            dur = st.text_input("No. DUR", dur_val, placeholder="No. DUR")
        with col3:
            sap = st.selectbox("SAP/Non", sap_option, index=tuple(sap_option["M"]).index(sap_val))

        col1, col2 = st.columns(2)
        with col1: 
            user = st.selectbox("User Name", user_option, index=tuple(user_option["M"]).index(user_val))
            tender = st.selectbox("Metode Tender", metode_tender_option, index=tuple(metode_tender_option["M"]).index(tender_val))
        with col2:
            vendor = st.selectbox("Vendor Name", vendor_option, index=tuple(vendor_option["M"]).index(vendor_val))
            status = st.text_input("Status", status_val, placeholder="Status")

        col1, col2, col3, col4 = st.columns(4)
        if data is not None:
            with col1:
                po_sched = getDate("PO Scheduled", data["PO Scheduled"][0])
            with col2:
                po_released = getDate("PO Released", data["PO Released"][0])
            with col3:
                eta = getDate("ETA", data["ETA"][0])
            with col4:
                bast = getDate("BAST", data["BAST"][0])
        else :
            with col1:
                po_sched = getDate("PO Scheduled")
            with col2:
                po_released = getDate("PO Released")
            with col3:
                eta = getDate("ETA")
            with col4:
                bast = getDate("BAST")
        
        col1, col2 = st.columns(2)
        with col1:
            delivtime = st.text_input("Delivery Time", deliv_val, placeholder="Delivery Time")
        with col2:
            penalty = st.text_input("Penalty", penalty_val, placeholder="Penalty")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            oe = st.number_input("OE", value=int(oe_val if oe_val is not None else 0), step=1000)
        with col2: 
            pook_v = st.number_input("PO/OK", value=int(pook_val if pook_val is not None else 0), step=1000)
        with col3:
            realization = st.number_input("Realization", value=int(realization_val if realization_val is not None else 0), step=1000)
        with col4:
            saving = st.number_input("Saving", value=int(saving_val if saving_val is not None else 0), step=1000)

        col1, col2 = st.columns([2,1])
        with col1:
            other = st.text_input("Other", other_val, placeholder="Other")
            file_loc = st.text_input("File Location", file_loc_val, placeholder="File Location")
        with col2:
            other2 = st.text_input("Other 2", other2_val, placeholder="Other 2")
            forecast = st.text_input("Forecast Realization", forecast_val, placeholder="Forecast Realization")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            cumulative = st.text_input("Cumulative FR", cumulative_val, placeholder="Cumulative FR")
        with col2:
            ir = st.text_input("IR Realization", ir_val, placeholder="IR Realization")
        with col3:
            a = st.text_input("A", a_val, placeholder="A")

    #===========================================#
    #------------------- SLA -------------------#
    #===========================================#
    with st.spinner("Loading SLA"):
        st.divider()
        st.header("SLA")
        st.write("Anda hanya dapat mengubah no.1, 2, 11 di SAP")
        # if "RETENDER" in tender:
        #     st.selectbox("Retender Start From", ["Created SR/MR", "PR Verified", "Izin Prinsip"])
        if data is not None:
            col1, col2, col3 = st.columns(3)
            with col1:
                sr_mr = getDate("1 Created SR/MR", data["Created SR/MR"][0], disabled=True)
                rfq = getDate("4 RFQ", data["RFQ"][0])
                nego = getDate("7 Klarifikasi & Negosiasi", data["Klarifikasi & Negosiasi"][0])
                awarding = getDate("10 Awarding", data["Awarding"][0])
            with col2:
                pr_verif = getDate("2 PR Verified by Daan", data["PR Verified by Daan"][0], disabled=True)
                offer = getDate("5 Penawaran Diterima", data["Penawaran diterima"][0])
                final_harga = getDate("8 Final Harga", data["Final Harga"][0])
                pook = getDate("11 PO/OK", data["PO_OK_SLA"][0], disabled=True)
            with col3:
                izin_prinsip = getDate("3 Izin Prinsip", data["Izin Prinsip"][0])
                tbe = getDate("6 TBE Diterima", data["TBE diterima"][0])
                rekomendasi = getDate("9 Rekomendasi PR", data["Rekomendasi PR"][0])
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                sr_mr = getDate("1 Created SR/MR")
                rfq = getDate("4 RFQ")
                nego = getDate("7 Klarifikasi & Negosiasi")
                awarding = getDate("10 Awarding")
            with col2:
                pr_verif = getDate("2 PR Verified by Daan")
                offer = getDate("5 Penawaran Diterima")
                final_harga = getDate("8 Final Harga")
                pook = getDate("11 PO/OK")
            with col3:
                izin_prinsip = getDate("3 Izin Prinsip")
                tbe = getDate("6 TBE Diterima")
                rekomendasi = getDate("9 Rekomendasi PR")
        
        col1, col2, col3, col4 = st.columns([1,1,1,6])
        with col1 : workday = st.text_input("Work Day", countWorkDay(start=sr_mr, end=pook), disabled=True)
        with col2 : actualday = st.text_input("Actual Day", countActualDay(start=sr_mr, end=pook), disabled=True)
        with col3 : slastat = st.text_input("Status", "RUMUSING", disabled=True)
        with col4 : remarks = st.text_input("Remarks", placeholder="Remarks")
            
        if data is not None:
            update = st.button("Update")
            if update :
                updateDataSLA(
                    id, selected_date, material_service, item_name, ka, rkap,
                            tpn, coa, discipline, eproc, dur, sap, user, vendor, status, tender, 
                            po_sched, po_released, eta, bast, delivtime, penalty, nomor_po, oe, 
                            pook_v, realization, saving, other, other2, file_loc, forecast, cumulative,
                            ir, a, tender, sr_mr, pr_verif, izin_prinsip, rfq, offer, tbe, nego, pook, final_harga, rekomendasi, 
                            awarding, actualday, slastat, remarks)
        else :
            create = st.button("Create")
            if create:
                insertDataSLA(
                    selected_date, material_service, item_name, ka, rkap,
                            tpn, coa, discipline, eproc, dur, sap, user, vendor, status, tender, 
                            po_sched, po_released, eta, bast, delivtime, penalty, nomor_po, oe, 
                            pook_v, realization, saving, other, other2, file_loc, forecast, cumulative,
                            ir, a, tender, sr_mr, pr_verif, izin_prinsip, rfq, offer, tbe, nego, pook, final_harga, rekomendasi, 
                            awarding, actualday, slastat, remarks)
    