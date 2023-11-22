import datetime
import streamlit as st
from data.getItemData import *

with st.spinner("Please Wait"):
    conn = create_snowflake_connection()
    cursor = conn.cursor()

    today = datetime.date.today()
    current_month = datetime.date.today().month
    month_range = range(1, 13)
    current_year = datetime.date.today().year
    year_range = range(current_year-3, current_year + 3)


    material_options = getMaterialOption(cursor)
    metode_tender_option = getTenderOption(cursor)
    ka_option = getKAOption(cursor)
    tpn_option = getJenisKebutuhan(cursor)
    coa_option = getCOAOption(cursor)
    discipline_option = getDisciplineOption(cursor)
    sap_option = getSapOption(cursor)
    eproc_option = getEprocOption(cursor)
    user_option = getUserOption(cursor)
    vendor_option = getVendorOption(cursor)
    cursor.close()
    conn.close()
