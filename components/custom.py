import streamlit as st
import numpy as np
from PIL import Image

def header():
    original_image = Image.open("components/piu.jpg")
    resized_image = original_image.resize((140, 100)) 

    col1, col2 = st.columns([1,2])
    with col1:
        st.image(resized_image)
    with col2:
        st.title("PRODA")

def getDate(label, date = None, disabled = False):
    if date is not None:
        box = st.checkbox(label, True, disabled=disabled)
        selected = st.date_input(label, date, label_visibility="collapsed", disabled=disabled, format="DD-MM-YYYY")
        if box:
            return selected
        else :
            return None
    else: 
        box = st.checkbox(label, False)
        selected = st.date_input(label, None, label_visibility="collapsed", format="DD-MM-YYYY")
        if box:
            return selected
        else :
            return None
    
def countWorkDay(start, end):
    if end == None or start == None:
        return 0
    else :
        return np.busday_count(start, end)
    
def countActualDay(start, end):
    if end == None or start == None:
        return 0
    else :
        return (end - start).days
    
def getSLA(tender):
    if tender == "Tender Umum":
        return 90
    elif tender == "Tender Terbatas":
        return 80
    elif tender == "Pemilihan Langsung":
        return 40
    elif tender == "Penunjukan Langsung":
        return 30
    elif tender == "Pengadaan Langsung":
        return 28
    else :
        return 0
    
def calculateSLA(tender, workday):
    SLA = getSLA(tender)
    if workday > SLA:
        return "LATE"
    elif workday < SLA:
        return "AHEAD"
    else:
        return "ON TIME"