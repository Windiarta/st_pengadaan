import streamlit as st
import pandas as pd
from modules.connection import create_snowflake_connection
from itertools import chain

def updateData(
        
):
    query = f"""UPDATE INTO DATA """

def insertSLA(
        prmonth, material, tender, created, verify, izin, rfq,
        penawaran, tbe, klarif, final, rekom, awarding,
        pook, actualday, workday, status, remarks
):
    query = f"""
        INSERT INTO PENGADAAN.PUBLIC.SLA1 (
            "PR Month",
            "Material / Service",
            "Item",
            "Metode Tender",
            "Created SR/MR",
            "PR Verified by Daan",
            "Izin Prinsip",
            RFQ,
            "Penawaran diterima",
            "TBE diterima",
            "Klarifikasi & Negosiasi",
            "Final Harga",
            "Rekomendasi PR",
            "Awarding",
            "PO/OK",
            "Actual Day Hari Kalender",
            "Hari Kerja",
            "Status",
            "REMARKS"
        ) VALUES (
            {prmonth},
            {material},
            {tender},
            {created},
            {verify},
            {izin},
            {rfq},
            {penawaran},
            {tbe},
            {klarif},
            {final},
            {rekom},
            {awarding},
            {pook},
            {actualday},
            {workday},
            {status},
            {remarks}
        );
        """
    return None

def insertData(prmonth, material, item, ka, rkap, ta, coa, disc,
            eproc, dur, sap, user, vendor, status, jenis, posched, 
            porelease, eta, bast, deliv, penal, nopook, oe, pook,
            real, save, other, other2, file, forecast, cumu, ir, a):
    query = f"""
        INSERT INTO PENGADAAN.PUBLIC.DATA (
            "PR Month",
            "Material/Services",
            "Item",
            "K/A",
            RKAP,
            "TA/Punchlist/Normal",
            COA,
            "Discipline",
            "E-Proc/PaDi/Normal",
            "No. DUR",
            "SAP/Non",
            "User Name",
            "Vendor Name",
            "Status",
            "Jenis Tender",
            "PO Scheduled",
            "PO Released",
            ETA,
            BAST,
            "Delivery Time",
            "Penalty/N",
            "No. PO/OK",
            OE,
            "PO/OK",
            "Realization",
            "Saving",
            "Other",
            "Other 2",
            "File Location",
            "Forecast Realization",
            "Cumulative FR",
            "IR Realization",
            A
        )
        VALUES (
            {prmonth}, {material}, {item}, {ka}, {rkap}, {ta}, {coa}, {disc},
            {eproc}, {dur}, {sap}, {user}, {vendor}, {status}, {jenis}, {posched}, 
            {porelease}, {eta}, {bast}, {deliv}, {penal}, {nopook}, {oe}, {pook},
            {real}, {save}, {other}, {other2}, {file}, {forecast}, {cumu}, {ir}, {a}
        );
        """
    return None
