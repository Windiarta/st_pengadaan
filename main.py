import streamlit as st
import pandas as pd
from datetime import date, datetime
from data.getItemData import *
from components.inputpo import *

header()

#=============================================#
#             STEP 1: Ambil Nomor             #
#=============================================#
def show_form():
    nomor = st.text_input("No. PO/OK Atau No. PR Atau No. SR/MR", value="6/MR-PIE/II/2021")
    if nomor == "":
        st.error("Nomor PO/OK Atau PR Atau SR/MR tidak boleh kosong!")
    else :
        with st.spinner("Loading Data"):
            #=============================================#
            #            STEP 2: Cari di SIMONA           #
            #=============================================#
            data_simona = getItemDetail(nomor)
            if data_simona.shape[0] == 1:
                index_simona = 0
            elif data_simona.shape[0] > 1:
                st.write(data_simona)
                index_simona = st.selectbox("Index Simona", range(0, data_simona.shape[0]-1))
            else:
                data_simona = None
                index_simona = 0

            #=============================================#
            #          STEP 3: Cari di Snowflake          #
            #=============================================#
            data_sf = getItemDetailFromData(nomor)
            if data_simona is not None and data_sf is None:
                nomor = data_simona["NO_PO"][index_simona]
            data_sf = getItemDetailFromData(nomor)
            if data_sf.shape[0] == 1:
                index = 0
            elif data_sf.shape[0] > 1:
                st.write(data_sf)
                index = st.selectbox("Index Revisi", range(0, data_sf.shape[0]-1))
            else:
                data_sf = None
                index = 0
            
            get_inputs(data_sf, data_simona, index, index_simona)

def show_report():
    end = date.today()
    col1, col2 = st.columns(2)
    with col1:
        start = st.date_input("Pilih Tanggal Awal", max_value=end)
    with col2:
        end = st.date_input("Pilih Tanggal Akhir", min_value=start, max_value=date.today())
    report_data = get_report_data(start, end)
    st.write(report_data)

tab1, tab2 = st.tabs(["Form", "Report"])
with tab1:
    show_form()
with tab2:
    show_report()