import streamlit as st
import pandas as pd
import random

excel_file_path = "data.xlsx"  # Excel 파일의 경로를 지정해야 합니다.
df = pd.read_excel(excel_file_path)

# Streamlit 앱 시작
st.title('데이터 프레임 표시')

# 데이터 프레임을 표로 표시
st.write(df)
