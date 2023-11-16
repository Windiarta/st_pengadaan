import streamlit as st
import numpy as np
from datetime import datetime

def getDate(label, date = None):
    if date is not None:
        box = st.checkbox(label, True)
        selected = st.date_input(label, date, label_visibility="collapsed", disabled=not box)
        if box:
            return selected
        else :
            return None
    else: 
        box = st.checkbox(label, False)
        selected = st.date_input(label, None, label_visibility="collapsed", disabled=not box)
        if box:
            return selected
        else :
            return None
    
def countWorkDay(start, end):
    if end == None or start == None:
        return 0
    else :
        np.busday_count(end, start)