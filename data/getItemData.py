from modules.connection import create_snowflake_connection
import pandas as pd

def getItemDetailByPO(po):
    return getResult(f"""SELECT * FROM DATAKU WHERE "No. PO/OK" = '{po}'""")

def getMaterialOption():
    return getResult(f"""SELECT DISTINCT(MATERIAL_SERVICE) AS m FROM DROPDOWN1 WHERE m IS NOT NULL;""")

def getTenderOption():
    return getResult(f"""SELECT DISTINCT(JENIS_TENDER) AS m FROM DROPDOWN1 WHERE m IS NOT NULL;""")

def getResult(query):
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    df = pd.DataFrame(result, columns=[desc[0] for desc in cursor.description])
    cursor.close()
    conn.close()
    return df