import streamlit as st
import numpy as np
from datetime import datetime

def getDate(label, date = None):
    box = st.checkbox(label, date is not None)
    date = st.date_input(label, date, label_visibility="collapsed", disabled=not box)
    if box:
        return date
    else :
        return None
    
def countWorkDay(start, end):
    if end == None or start == None:
        return 0
    else :
        np.busday_count(end, start)