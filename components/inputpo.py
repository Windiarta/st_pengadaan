import streamlit as st
from data.const import *
from data.sendData import *
from components.custom import *
from data.getItemDetail import *


def get_inputs(data, datasimona, index=0, indexsimona=0):
    #=============================================#
    #----------------- VAR INIT ------------------#
    #=============================================#
    st.write("DATA SLA")
    st.write(data)
    st.write("SIMONA")
    st.write(datasimona)

    # SET DEFAULT VALUE
    if datasimona is not None:
        no_mr_sr = datasimona["NO_MR_SR"][indexsimona]
        no_pr = datasimona["NO_PR"][indexsimona]
        no_po = datasimona["NO_PO"][indexsimona]
    else:
        if data is not None:
            no_mr_sr = data["No. MR/SR"][index] if data["No. MR/SR"][index] is not None else ''
            no_pr = data["No. PR"][index] if data["No. PR"][index] is not None else ''
            no_po = data["No. PO/OK"][index] if data["No. PO/OK"][index] is not None else ''
        else:
            no_mr_sr = ''
            no_pr = ''
            no_po = ''
    
    # Code dibawah ini berfungsi untuk mengassign data simona dan data
    id_val, date_val, material_val, tender_val, item_val, ka_val, rkap_val, tpn_val, coa_val, discipline_val, eproc_val, dur_val, sap_val, user_val, vendor_val, status_val, poreleased_val, eta_val, bast_val, deliv_val, penalty_val, oe_val, pook_val, realization_val, saving_val, other_val, void_val = get_data_index(data, datasimona, index, indexsimona)
    
    #=============================================#
    #------------------- DATA --------------------#
    #=============================================#
    with st.spinner("Loading Data"):
        st.divider()
        st.header("DATA")

        item_name = st.text_input("Item", item_val, placeholder="Item Name")

        col1, col2, col3 = st.columns(3)
        newmr = col1.text_input("No. MR/SR", no_mr_sr, disabled=datasimona is not None, placeholder="No. MR/SR")
        newpr = col2.text_input("No. PR", no_pr, disabled=datasimona is not None, placeholder="No. PR")
        newpo = col3.text_input("No. PO/OK", no_po, disabled=datasimona is not None, placeholder="No. PO/OK")

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

        vdr_index = vendor_val if vendor_val in vendor_option else None
        if vdr_index == vendor_val:
            col1, col2 = st.columns(2)
            user = col1.text_input("User Name", user_val, placeholder="User Name")
            vendor = col2.selectbox("Vendor Name", vendor_option, index=tuple(vendor_option["M"]).index(vdr_index))
        else:
            col1, col2, col3 = st.columns(3)
            user = col1.text_input("User Name", user_val, placeholder="User Name")
            col2.write(vendor_val)
            vendor = col3.selectbox("Vendor Name", vendor_option, index=tuple(vendor_option["M"]).index(None), placeholder=vendor_val)

        col1, col2 = st.columns(2)
        with col1: 
            tender = st.selectbox("Metode Tender", metode_tender_option, index=tuple(metode_tender_option["M"]).index(tender_val))
        with col2:
            status = st.text_input("Status", status_val, placeholder="Status")

        col2, col3, col4 = st.columns(3)
        if data is not None:
            with col2:
                po_released = getDate("PO Released", poreleased_val)
            with col3:
                eta = getDate("ETA", eta_val)
            with col4:
                bast = getDate("BAST", bast_val)
        else :
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
            try:
                penalty_val = countActualDay(eta, bast if bast is not None else today)
            except:
                st.write(penalty_val)
            penalty = st.text_input("Penalty (BAST - ETA)", penalty_val, placeholder="Penalty")

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            oe = st.number_input("OE", value=int(oe_val if oe_val is not None else 0), step=1000)
        with col2: 
            pook_v = st.number_input("PO/OK", value=int(pook_val if pook_val is not None else 0), step=1000)
        with col3:
            realization = st.number_input("Realization", value=int(realization_val if realization_val is not None else 0), step=1000)
        with col4:
            saving = st.number_input("Saving", value=int(saving_val if saving_val is not None else 0), step=1000)

        other = st.text_area("Other", other_val, placeholder="Other")
        

    #===========================================#
    #------------------- SLA -------------------#
    #===========================================#

    with st.spinner("Loading SLA"):
        st.divider()
        st.header("SLA")
        st.write("Anda hanya dapat mengubah no.1, 2, 11 di SAP")
        st.write(datasimona)
        if data is not None:
            col1, col2, col3 = st.columns(3)
            with col1:
                if datasimona is not None:
                    sr_mr = getDate("1 Created SR/MR", datasimona["Created SR/MR"][0], disabled=True)
                else :
                    sr_mr = getDate("1 Created SR/MR", data["Created SR/MR"][0])
                rfq = getDate("4 RFQ", data["RFQ"][0])
                nego = getDate("7 Klarifikasi & Negosiasi", data["Klarifikasi & Negosiasi"][0])
                awarding = getDate("10 Awarding", data["Awarding"][0])
            with col2:
                if datasimona is not None:
                    pr_verif = getDate("2 PR Verified by Daan", datasimona["PR Verified by Daan"][0], disabled=True)
                else :
                    pr_verif = getDate("2 PR Verified by Daan", data["PR Verified by Daan"][0])
                offer = getDate("5 Penawaran Diterima", data["Penawaran diterima"][0])
                final_harga = getDate("8 Final Harga", data["Final Harga"][0])
                if datasimona is not None:
                    pook = getDate("11 PO/OK", datasimona["PO_OK_SLA"][0], disabled=True)
                else:
                    pook = getDate("11 PO/OK", data["PO_OK_SLA"][0])
            with col3:
                izin_prinsip = getDate("3 Izin Prinsip", data["Izin Prinsip"][0])
                tbe = getDate("6 TBE Diterima", data["TBE diterima"][0])
                rekomendasi = getDate("9 Rekomendasi PR", data["Rekomendasi PR"][0])
        else:
            col1, col2, col3 = st.columns(3)
            with col1:
                if datasimona is not None:
                    sr_mr = getDate("1 Created SR/MR", datasimona["Created SR/MR"][0], disabled=True)
                else:
                    sr_mr = getDate("1 Created SR/MR")
                rfq = getDate("4 RFQ")
                nego = getDate("7 Klarifikasi & Negosiasi")
                awarding = getDate("10 Awarding")
            with col2:
                if datasimona is not None:
                    pr_verif = getDate("2 PR Verified by Daan", datasimona["PR Verified by Daan"][0], disabled=True)
                else:
                    pr_verif = getDate("2 PR Verified by Daan")
                offer = getDate("5 Penawaran Diterima")
                final_harga = getDate("8 Final Harga")
                if datasimona is not None:
                    pook = getDate("11 PO/OK", datasimona["PO_OK_SLA"][0], disabled=True)
                else :
                    pook = getDate("11 PO/OK")
            with col3:
                izin_prinsip = getDate("3 Izin Prinsip")
                tbe = getDate("6 TBE Diterima")
                rekomendasi = getDate("9 Rekomendasi PR")
        
        
        col1, col2, col3, col4 = st.columns([4, 1, 1, 1])
        with col1:
            status_tender = st.selectbox("Status Tender (VOID)", ["None", "Retender", "Cancelled"], disabled=material_service!="VOID")
        with col2 : workday = st.text_input("Work Day", countWorkDay(start=sr_mr, end=pook), disabled=True)
        with col3 : actualday = st.text_input("Actual Day", countActualDay(start=sr_mr, end=pook), disabled=True)
        with col4 : slastat = st.text_input("Status", calculateSLA(tender_val, int (workday)), disabled=True)
        remarks = st.text_area("Remarks", placeholder="Remarks")
            
        if data is None:
            create = st.button("Create")
            update = False
            
        if data is not None:
            create = st.button("Create")
            update = st.button("Update")
        
        if create :
            if (newmr != '' and newpr != '' and newpo != ''):
                with st.spinner("Inserting Data"):
                    insertDataSLA(
                        selected_date, material_service, item_name, ka, rkap,
                            tpn, coa, discipline, eproc, dur, sap, user, vendor, status, tender, status_tender,
                            po_released, eta, bast, delivtime, penalty, newpo, oe, 
                            pook_v, realization, saving, other, sr_mr, pr_verif, izin_prinsip, rfq, offer, tbe, nego, pook, 
                            final_harga, rekomendasi, awarding, actualday, slastat, remarks, newmr, newpr)
            else :
                st.error("Isi Nomor MR/SR, Nomor PR, atau Nomor PO/OK agar dapat menginput data")
                
        if update : 
            if (newmr != '' and newpr != '' and newpo != ''):
                with st.spinner("Updating Data"):
                    updateDataSLA(
                        id, selected_date, material_service, item_name, ka, rkap,
                            tpn, coa, discipline, eproc, dur, sap, user, vendor, status, tender, status_tender,
                            po_released, eta, bast, delivtime, penalty, newpo, oe, 
                            pook_v, realization, saving, other, sr_mr, pr_verif, izin_prinsip, rfq, offer, tbe, nego, pook, 
                            final_harga, rekomendasi, awarding, actualday, slastat, remarks, newmr, newpr)
            else :
                st.error("Isi Nomor MR/SR, Nomor PR, atau Nomor PO/OK agar dapat menginput data")
