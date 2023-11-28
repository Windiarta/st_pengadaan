import streamlit as st
from data.const import today
from modules.connection import create_snowflake_connection

def execQuery(query):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    cursor.close()
    conn.close()
    st.success("Aksi Berhasil")

def insertDataSLA(prmonth='', material='', item='', ka='', rkap='', ta='', coa='', disc='',
            eproc='', dur='', sap='', user='', vendor='', status='', jenis='', void='',
            porelease=None, eta=None, bast=None, deliv='', penal='', nopook=None, oe='', pook='',
            real='', save='', other='', created=None, verify=None, izin=None, rfq=None, penawaran=None, tbe=None, 
            klarif=None, pooksla=None, final=None, rekom=None, awarding=None, actualday='', 
            slastat='', remarks='', no_mr_sr=None, no_pr=None):
    query = f"""
    INSERT INTO PENGADAAN.PUBLIC.DATASLA ( "PR Month", "Material/Services", "Item", "K/A", RKAP, "TA/Punchlist/Normal", COA, 
    "Discipline", "E-Proc/PaDi/Normal", "No. DUR", "SAP/Non", "User Name", "Vendor Name", "Status", "Jenis Tender", "Status Void", 
    "PO Released", ETA, BAST, "Delivery Time", "Penalty/N", "No. PO/OK", OE, "PO/OK", "Realization", "Saving", "Other", "Created SR/MR", "PR Verified by Daan", 
    "Izin Prinsip", RFQ, "Penawaran diterima", "TBE diterima", "Klarifikasi & Negosiasi", "Rekomendasi PR", "Awarding", PO_OK_SLA, 
    "Actual Day Hari Kalender", "Final Harga", STATUS_SLA, "REMARKS", "CREATED_AT", "No. MR/SR", "No. PR" ) VALUES 
    (
        '{prmonth}', '{material}', '{item}', '{ka}', '{rkap}', '{ta}', '{coa}', '{disc}',
        '{eproc}', '{dur}', '{sap}', '{user}', '{vendor}', '{status}', '{jenis}', '{void}',
        {"NULL" if porelease is None else f"'{porelease}'"}, {'NULL' if eta is None else f"'{eta}'"}, {'NULL' if bast is None else f"'{bast}'"},
        '{deliv}', '{penal}', {'NULL' if nopook == '' else f"'{nopook}'"}, '{oe}', '{pook}',
        '{real}', '{save}', '{other}', {'NULL' if created is None else f"'{created}'"}, {'NULL' if verify is None else f"'{verify}'"}, 
        {'NULL' if izin is None else f"'{izin}'"}, {'NULL' if rfq is None else f"'{rfq}'"}, {'NULL' if penawaran is None else f"'{penawaran}'"},
        {'NULL' if tbe is None else f"'{tbe}'"}, {'NULL' if klarif is None else f"'{klarif}'"},
        {'NULL' if rekom is None else f"'{rekom}'"}, {'NULL' if awarding is None else f"'{awarding}'"}, 
        {'NULL' if pooksla is None else f"'{pooksla}'"}, '{actualday}', {'NULL' if final is None else f"'{final}'"}, '{slastat}', '{remarks}',
        '{today}', {'NULL' if no_mr_sr == '' else f"'{no_mr_sr}'"}, {'NULL' if no_pr == '' else f"'{no_pr}'"}
    );
    """
    execQuery(query)



def updateDataSLA(id_value, prmonth='', material='', item='', ka='', rkap='', ta='', coa='', disc='',
            eproc='', dur='', sap='', user='', vendor='', status='', jenis='', void='',
            porelease=None, eta=None, bast=None, deliv='', penal='', nopook='', oe='', pook='',
            real='', save='', other='', created=None, verify=None, izin=None, rfq=None, penawaran=None, tbe=None, 
            klarif=None, pooksla=None, final=None, rekom=None, awarding=None, actualday='', 
            slastat='', remarks='', no_mr_sr='', no_pr=''):
    porelease = 'NULL' if porelease is None else f"'{porelease}'"
    eta = 'NULL' if eta is None else f"'{eta}'"
    bast = 'NULL' if bast is None else f"'{bast}'"
    created = 'NULL' if created is None else f"'{created}'"
    verify = 'NULL' if verify is None else f"'{verify}'"
    izin = 'NULL' if izin is None else f"'{izin}'"
    rfq = 'NULL' if rfq is None else f"'{rfq}'"
    penawaran = 'NULL' if penawaran is None else f"'{penawaran}'"
    tbe = 'NULL' if tbe is None else f"'{tbe}'"
    klarif = 'NULL' if klarif is None else f"'{klarif}'"
    rekom = 'NULL' if rekom is None else f"'{rekom}'"
    awarding = 'NULL' if awarding is None else f"'{awarding}'"
    pooksla = 'NULL' if pooksla is None else f"'{pooksla}'"
    final = 'NULL' if final is None else f"'{final}'"
    
    query = f"""
        UPDATE PENGADAAN.PUBLIC.DATASLA SET 
            "PR Month" = '{prmonth}', 
            "Material/Services" = '{material}', 
            "Item" = '{item}', 
            "K/A" = '{ka}', 
            RKAP = '{rkap}', 
            "TA/Punchlist/Normal" = '{ta}', 
            COA = '{coa}', 
            "Discipline" = '{disc}',
            "E-Proc/PaDi/Normal" = '{eproc}', 
            "No. DUR" = '{dur}', 
            "SAP/Non" = {f"'{sap}'" if (sap != '' and sap is not None) else "NULL"}, 
            "User Name" = '{user}', 
            "Vendor Name" = '{vendor}', 
            "Status" = '{status}', 
            "Jenis Tender" = '{jenis}', 
            "PO Released" = {porelease}, 
            ETA = {eta}, 
            BAST = {bast}, 
            "Delivery Time" = '{deliv}', 
            "Penalty/N" = '{penal}', 
            "No. PO/OK" = '{nopook}', 
            OE = '{oe}', 
            "PO/OK" = '{pook}',
            "Realization" = '{real}', 
            "Saving" = '{save}', 
            "Other" = '{other}', 
            "Status Void" = '{void}', 
            "Created SR/MR" = {created}, 
            "PR Verified by Daan" = {verify}, 
            "Izin Prinsip" = {izin}, 
            RFQ = {rfq}, 
            "Penawaran diterima" = {penawaran}, 
            "TBE diterima" = {tbe}, 
            "Klarifikasi & Negosiasi" = {klarif},
            "Rekomendasi PR" = {rekom}, 
            "Awarding" = {awarding}, 
            PO_OK_SLA = {pooksla}, 
            "Actual Day Hari Kalender" = {actualday},
            "Final Harga" = {final}, 
            STATUS_SLA = '{slastat}', 
            "REMARKS" = '{remarks}',
            "No. MR/SR" = '{no_mr_sr}', 
            "No. PR" = '{no_pr}'
        WHERE ID = {id_value};"""
    execQuery(query)