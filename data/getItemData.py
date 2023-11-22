from modules.connection import create_snowflake_connection
import pandas as pd

def getItemDetailByPO(po):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    df = getResult(cursor, f"""SELECT * FROM DATASLA WHERE "No. PO/OK" = '{po}'""")
    cursor.close()
    conn.close()
    return df

def getMaterialOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT(MATERIAL_SERVICES) AS m FROM DROPDOWN WHERE m IS NOT NULL;""")

def getTenderOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT(JENIS_TENDER) AS m FROM DROPDOWN WHERE m IS NOT NULL;""")

def getVendorOption(cursor):
    return getResult(cursor, f"""SELECT vendor as m FROM VENDORS;""")

def getKAOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("K/A") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getJenisKebutuhan(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("Jenis Kebutuhan") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getCOAOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("COA") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getDisciplineOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("Discipline") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getSapOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("SAP/Non") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getEprocOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("E-Proc/PaDi/Normal") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getUserOption(cursor):
    return getResult(cursor, f"""SELECT DISTINCT("User") AS m FROM DROPDOWN""")

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

