import streamlit as st
from data.getItemData import *
from components.custom import *
from components.input import *
        
header()

col1, col2 = st.columns([1, 2])
with col1 : source = st.selectbox("Data Source", ["SAP", "PADI", "SIMONA", "Manual"])
with col2 : nomor_po = st.text_input("No. PO/OK", value="5900000489")

if nomor_po == "":
    st.error("Nomor PO tidak boleh kosong!")
else :
    data = getItemDetailByPO(nomor_po)
    if data.shape[0] == 1:
        get_inputs(data, nomor_po)
    elif(data.shape[0] > 1):
        st.write(data)
        index = st.selectbox("Index", range(0, data.shape[0]))
        get_inputs(data, nomor_po, index)
    else :
        get_inputs(None, nomor_po)



