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
    nomor = st.text_input("No. PO/OK atau No. PR atau No. SR/MR atau (ID Data tidak terintegrasi SIMONA)", placeholder="\"CREATE\" untuk memasukan data baru")
    if nomor.upper() == "CREATE":
        get_inputs(None, None)
    else:
        if nomor == "":
            st.warning("Masukan Nomor PO/OK atau PR atau SR/MR untuk mencari data")
            st.warning("Masaukan CREATE untuk menginput data")
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
                # data_sf = getItemDetailFromData(nomor)
                # st.write(data_sf.iloc[0])
                # if data_simona is not None and data_sf is None:
                #     nomor = data_simona["NO_PO"][index_simona]
                data_sf = getItemDetailFromData(nomor)
                if data_sf.shape[0] == 1:
                    index = 0
                elif data_sf.shape[0] > 1:
                    st.write(data_sf)
                    index = st.selectbox("Index Revisi", range(0, data_sf.shape[0]-1))
                else:
                    data_sf = None
                    index = 0

                if data_simona is None and data_sf is None:
                    st.error('Input tidak ditemukan, gunakan kata kunci \"CREATE\" untuk menginput data')
                else:                
                    success = get_inputs(data_sf, data_simona, index, index_simona)
                    if success:
                        st.success("Aksi berhasil")

def show_report():
    end = date.today()
    with st.form("Report"):
        col1, col2 = st.columns(2)
        with col1:
            start = st.date_input("Pilih Tanggal Awal", max_value=end)
        with col2:
            end = st.date_input("Pilih Tanggal Akhir", min_value=start)
        report_data = get_report_data(start, end)
        show = st.form_submit_button("Show Data")
    if show : 
        if report_data is not None:
            st.write(report_data)
            st.download_button("Download CSV", report_data.to_csv().encode('utf-8'), file_name=f"report_{start}_{end}.csv", mime='text/csv')
        else:
            st.write("Tidak ada data")

tab1, tab2 = st.tabs(["Form", "Report"])
with tab1:
    show_form()
with tab2:
    show_report()