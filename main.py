import streamlit as st
from data.getItemData import *
from data.const import *
from components.custom import *

# Judul aplikasi
st.title("PENGADAAN")

def get_inputs(data):
    if data is not None:
        st.write(data)
        date_val = data["PR Month"][0]
        material_val = data["Material/Services"][0]
        tender_val = data["Status Tender"][0]
    else:
        st.warning("Tidak ada data, Isi untuk menginput data baru")
        date_val = today
        material_val = material_options[0][0]
        tender_val = metode_tender_option[0]

    col1, col2 = st.columns([1, 2])
    with col1: 
        selected_date = st.date_input("PR Month", date_val)
    with col2:        
        meterial_service = st.selectbox("Material/Service", material_options, index=tuple(material_options["M"]).index(material_val))

    tender = st.selectbox("Metode Tender", metode_tender_option, index=tuple(metode_tender_option["M"]).index(tender_val))
    
    col1, col2, col3 = st.columns(3)
    with col1:
        sr_mr = getDate("1 Created SR/MR", data["Created SR/MR"][0])
        rfq = getDate("4 RFQ", data["RFQ"][0])
        nego = getDate("7 Klarifikasi & Negosiasi", data["Klarifikasi & Negosiasi"][0])
        awarding = getDate("10 Awarding", data["Awarding"][0])
    with col2:
        pr_verif = getDate("2 PR Verified by Daan", data["PR Verified by Daan"][0])
        offer = getDate("5 Penawaran Diterima", data["Penawaran diterima"][0])
        final_harga = getDate("8 Final Harga", data["Final Harga"][0])
        pook = getDate("11 PO/OK", data["PO_OK_SLA"][0])
    with col3:
        izin_prinsip = getDate("3 Izin Prinsip", data["Izin Prinsip"][0])
        tbe = getDate("6 TBE Diterima", data["TBE diterima"][0])
        rekomendasi = getDate("9 Rekomendasi PR", data["Rekomendasi PR"][0])

    col1, col2, col3 = st.columns([1,1,4])
    with col1 : workday = st.text_input("Work Day", countWorkDay(start=sr_mr, end=pook), disabled=True)
    with col2 : status = st.text_input("Status", "RUMUSING", disabled=True)
    with col3 : remarks = st.text_input("Remarks", placeholder="Remarks")


    

col1, col2 = st.columns([1, 2])
with col1 : source = st.selectbox("Data Source", ["SAP", "PADI", "SIMONA", "Manual"])
with col2 : nomor_po = st.text_input("No. PR/PO", value="5900000489")

if nomor_po == "":
    st.error("Nomor PO tidak boleh kosong!")
else :
    data = getItemDetailByPO(nomor_po)
    st.write(data)
    if data.shape[0] == 1:
        get_inputs(data)
    else :
        get_inputs(None)

st.button("Save")


