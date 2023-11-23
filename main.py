import streamlit as st
from data.getItemData import *
from components.inputpo import *

header()

nomor = st.text_input("No. PO/OK Atau No. PR Atau No. SR/MR", value="6/MR-PIE/II/2021")
if nomor == "":
    st.error("Nomor PO/OK Atau PR Atau SR/MR tidak boleh kosong!")
else :
    with st.spinner("Loading Data"):
        data = getItemDetail(nomor)
        st.write(data)
        data = getItemDetailFromData(nomor)
        st.write(data)
    
    if data.shape[0] == 1:
        get_inputs(data, nomor)
    elif(data.shape[0] > 1):
        st.write(data)
        index = st.selectbox("Index", range(0, data.shape[0]))
        get_inputs(data, nomor, index)
    else :
        get_inputs(None, nomor)
        


