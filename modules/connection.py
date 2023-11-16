import json
import streamlit as st
from snowflake.snowpark import Session
import snowflake.connector

def create_snowflake_connection():
    connection = snowflake.connector.connect(
            user=st.secrets["DB_USER"],
            password=st.secrets["DB_PASSWORD"],
            account=st.secrets["DB_ACCOUNT"],
            warehouse=st.secrets["DB_WAREHOUSE"],
            database=st.secrets["DB_DATABASE"],
            schema=st.secrets["DB_SCHEMA"],
            role = st.secrets["DB_ROLE"]
    )
    return connection
