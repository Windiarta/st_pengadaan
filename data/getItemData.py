from modules.connection import create_snowflake_connection
import pandas as pd

def getItemDetail(nomor):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    df = getResult(cursor, f"""
            SELECT DISTINCT
                a.NO_MR_SR, MRSR.TGL_MRSR AS "Created SR/MR", 
                a.NO_PR, PR.TGL_PR AS "PR Month", YEAR(PR.TGL_PR) AS "RKAP",
                PR.VERIFIED_BY_DAAN AS "PR Verified by Daan",
                a.NO_PO, PO.TGL_PO AS "PO_OK_SLA", PO.PO_RELEASE AS "PO Released", PO."ETA" AS "ETA",
                a.URAIAN AS "Item", a.NAMAVENDOR AS "Vendor Name", "Material/Services",
                DUR."E-Proc/PaDi/Normal", DUR.NO_DUR AS "No. DUR", DUR."SAP/Non", DUR.OE AS "OE",
                USR.NAME AS "User Name", a."PO/OK", 
                CASE WHEN DUR.METODE_PENGADAAN_NAME = 'Lelang Terbuka' THEN 'Tender Umum'
                WHEN DUR.METODE_PENGADAAN_NAME = 'Lelang Terbatas' THEN 'Tender Terbatas'
                WHEN DUR.METODE_PENGADAAN_NAME = 'Penunjukkan Langsung' THEN 'Penunjukan Langsung'
                ELSE DUR.METODE_PENGADAAN_NAME END AS "Jenis Tender"
                FROM 
                    (SELECT 
                        NO_MR_SR, a.NO_PR AS NO_PR, b.PO_NO AS NO_PO, 
                        URAIAN, NAMAVENDOR, COMP_CODE, "Material/Services", CREATED_BY, PO_TOTAL AS "PO/OK"
                    FROM (
                        SELECT x.NO_MR_SR AS NO_MR_SR, COMP_CODE, NO_PR, x.URAIAN, CREATED_BY, 'M' AS "Material/Services"
                        FROM SIMONA.PUBLIC.MR x
                        LEFT JOIN SIMONA.PUBLIC.VW_MRPR y
                        ON x.NO_MR_SR = y.NO_MR_SR
                        WHERE COMP_CODE LIKE 'J%'
                        UNION ALL
                        SELECT x.NO_MR_SR AS NO_MR_SR, COMP_CODE, NO_PR, x.URAIAN, CREATED_BY, 'S' AS "Material/Services"
                        FROM SIMONA.PUBLIC.SR x
                        LEFT JOIN SIMONA.PUBLIC.VW_SRPR y
                        ON x.NO_MR_SR = y.NO_MR_SR
                        WHERE COMP_CODE LIKE 'J%') a 
                    FULL OUTER JOIN SIMONA.PUBLIC.VW_OEPO b 
                    ON a.NO_PR = b.NO_PR
                    WHERE 
                        NO_MR_SR = '{nomor}' OR
                        a.NO_PR = '{nomor}' OR
                        NO_PO = '{nomor}') a 
                LEFT JOIN
                    (SELECT NO_MR_SR, TANGGAL AS TGL_MRSR 
                    FROM SIMONA.PUBLIC.MR 
                    WHERE COMP_CODE = 'J000' 
                    UNION ALL
                    SELECT NO_MR_SR, TANGGAL AS TGL_MRSR 
                    FROM SIMONA.PUBLIC.SR 
                    WHERE COMP_CODE = 'J000') MRSR
                    ON a.NO_MR_SR = MRSR.NO_MR_SR
                LEFT JOIN
                    (SELECT NO_PR, TGL_PR, VERIFIED_BY_DAAN 
                    FROM SIMONA.PUBLIC.PR_GOODS 
                    WHERE COMP_CODE = 'J000'
                    UNION ALL
                    SELECT NO_PR, TGL_PR, VERIFIED_BY_DAAN 
                    FROM SIMONA.PUBLIC.PR_SVC 
                    WHERE COMP_CODE = 'J000') PR 
                    ON a.NO_PR = PR.NO_PR
                LEFT JOIN 
                    (SELECT PO_NO AS NO_PO, PO_DATE AS TGL_PO, PO_RELEASE, d.DELIVERY_DATE AS "ETA"
                    FROM SIMONA.PUBLIC.PO_GOODS c LEFT JOIN SIMONA.PUBLIC.PO_GOODS_ITEM d ON c.PO_GOODS_ID = d.PO_GOODS_ID
                    WHERE COMP_CODE = 'J000'
                    UNION ALL
                    SELECT PO_NO AS NO_PO, PO_DATE AS TGL_PO, PO_RELEASE, d.DELIVERY_DATE AS "ETA"
                    FROM SIMONA.PUBLIC.PO_SVC c LEFT JOIN SIMONA.PUBLIC.PO_SVC_ITEM d ON c.PO_SVC_ID = d.PO_SVC_ID
                    WHERE COMP_CODE = 'J000') PO 
                    ON a.NO_PO = PO.NO_PO
                LEFT JOIN 
                    (SELECT CASE WHEN SISTEM_PENGADAAN != 'SAP' THEN SISTEM_PENGADAAN ELSE NULL END AS "E-Proc/PaDi/Normal", 
                    NO_DUR, CASE WHEN SISTEM_PENGADAAN = 'SAP' THEN 'SAP' ELSE NULL END AS "SAP/Non", NO_PR, NO_MR_SR,
                    TOTAL AS OE, METODE_PENGADAAN_NAME
                    FROM SIMONA.PUBLIC.VW_TR_DUR_GOODS_FINAL
                    UNION ALL
                    SELECT CASE WHEN SISTEM_PENGADAAN != 'SAP' THEN SISTEM_PENGADAAN ELSE NULL END AS "E-Proc/PaDi/Normal", 
                    NO_DUR, CASE WHEN SISTEM_PENGADAAN = 'SAP' THEN 'SAP' ELSE NULL END AS "SAP/Non", NO_PR, NO_MR_SR,
                    TOTAL AS OE, METODE_PENGADAAN_NAME
                    FROM SIMONA.PUBLIC.VW_TR_DUR_SVC_FINAL) DUR
                    ON a.NO_PR = DUR.NO_PR OR a.NO_MR_SR = DUR.NO_MR_SR
                LEFT JOIN 
                    (SELECT KODE_USER, NAME 
                    FROM SIMONA.PUBLIC.USER 
                    WHERE COMP_CODE = 'J000') USR
                    ON a.CREATED_BY = USR.KODE_USER
                ;""")
    cursor.close()
    conn.close()
    return df

def getItemDetailFromData(nomor):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    df = getResult(cursor, f"""SELECT * FROM DATASLA WHERE 
                   "No. PO/OK" = '{nomor}' OR 
                   "No. PR" = '{nomor}' OR 
                   "No. MR/SR" = '{nomor}' OR
                   "ID" = TRY_TO_NUMBER('{nomor}')""")
    cursor.close()
    conn.close()
    return df

def getMaterialOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT(MATERIAL_SERVICES) AS m FROM DROPDOWN WHERE m IS NOT NULL;""")

def getTenderOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT(JENIS_TENDER) AS m FROM DROPDOWN;""")

def getVendorOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT(NAMA) AS m FROM SIMONA.PUBLIC.MS_VENDOR WHERE COMP_CODE = 'J000' UNION ALL SELECT null AS m;""")

def getKAOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("K/A") AS m FROM DROPDOWN""")

def getJenisKebutuhan(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("Jenis Kebutuhan") AS m FROM DROPDOWN""")

def getCOAOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("COA") AS m FROM DROPDOWN UNION SELECT DISTINCT("COA") AS m FROM DATASLA""")

def getDisciplineOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("Discipline") AS m FROM DROPDOWN""")

def getSapOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("SAP/Non") AS m FROM DROPDOWN""")

def getEprocOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("E-Proc/PaDi/Normal") AS m FROM DATASLA""")

def getUserOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("User") AS m FROM DROPDOWN""")

def get_report_data(start, end):
    return getResult(None, f"""SELECT * FROM DATASLA1 WHERE CREATED_AT BETWEEN '{start}' AND '{end}'""")

    
def getResult(cursor=None, query=None):
    if cursor is None:
        conn = create_snowflake_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
        cursor.close()
        conn.close()
    else :
        cursor.execute(query)
        result = cursor.fetchall()
        df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
    return df


