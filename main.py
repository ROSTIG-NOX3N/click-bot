import streamlit as st
import pandas as pd

# Excel 파일의 경로를 지정해야 합니다.
excel_file_path = "data.xlsx"

# Streamlit 앱 시작
st.title('데이터 프레임 표시')

# Excel 파일을 데이터 프레임으로 읽어오기
try:
    df = pd.read_excel(excel_file_path)
    st.write(df)
except FileNotFoundError:
    st.error(f"파일을 찾을 수 없습니다: {excel_file_path}")
except Exception as e:
    st.error(f"데이터 프레임을 로드하는 중 오류 발생: {e}")
