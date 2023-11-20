from modules.connection import create_snowflake_connection
import pandas as pd

def getItemDetailByPO(po):
    return getResult(f"""SELECT * FROM DATAKU WHERE "No. PO/OK" = '{po}'""")

def getMaterialOption():
    return getResult(f"""SELECT DISTINCT(MATERIAL_SERVICES) AS m FROM DROPDOWN WHERE m IS NOT NULL;""")

def getTenderOption():
    return getResult(f"""SELECT DISTINCT(JENIS_TENDER) AS m FROM DROPDOWN WHERE m IS NOT NULL;""")

def getVendorOption():
    return getResult(f"""SELECT DISTINCT("Row Labels") AS m FROM VENDORLIST""")

def getKAOption():
    return getResult(f"""SELECT DISTINCT("K/A") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getJenisKebutuhan():
    return getResult(f"""SELECT DISTINCT("Jenis Kebutuhan") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getCOAOption():
    return getResult(f"""SELECT DISTINCT("COA") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getDisciplineOption():
    return getResult(f"""SELECT DISTINCT("Discipline") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getSapOption():
    return getResult(f"""SELECT DISTINCT("SAP/Non") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getEprocOption():
    return getResult(f"""SELECT DISTINCT("E-Proc/PaDi/Normal") AS m FROM DROPDOWN WHERE m IS NOT NULL""")

def getUserOption():
    return getResult(f"""SELECT DISTINCT("User") AS m FROM DROPDOWN""")

def getResult(query):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
    cursor.close()
    conn.close()
    return df