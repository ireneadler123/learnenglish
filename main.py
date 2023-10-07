import streamlit as st
import mysql
import mysql.connector
st.set_page_config(page_title = 'Learning English with me', page_icon = ':earth_asia:', layout = 'wide')



conn = mysql.connector.connect(
    host="learn-english.cultise206ef.ap-southeast-2.rds.amazonaws.com",
    user="admin",
    password="12121993",
    database="learn-english",
    port=3306
)
