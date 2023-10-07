import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import os
import matplotlib.pyplot as plt
import warnings
import mysql.connector
from datetime import datetime, timedelta
from datetime import datetime
warnings.filterwarnings('ignore')
st.set_page_config(page_title = 'Learning English with me', page_icon = ':earth_asia:', layout = 'wide')



conn = mysql.connector.connect(
    host="learn-english.cultise206ef.ap-southeast-2.rds.amazonaws.com",
    user="irene",
    password="12121993",
    database="learn-english",
    port=3306
)

# cursor = conn.cursor()

# cursor.execute("CREATE USER 'irene'@'learn-english.cultise206ef.ap-southeast-2.rds.amazonaws.com' IDENTIFIED WITH 'caching_sha2_password' BY '12121993'")
# conn.commit()