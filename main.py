import streamlit as st
import pandas as pd
import openpyxl
# Excel 파일을 읽고 데이터 가져오기
df = pd.read_excel("data.xlsx")

def bring_data():
    spots_df = df[df['분류'] == '관광지']
    spots_df = spots_df.reset_index(drop=True)
    Q = spots_df['질문']
    P = spots_df['장소']
    A = spots_df['답변']
    latitude = spots_df['위도']
    longitude = spots_df['경도']
    
    return Q, P, A, latitude, longitude

Q, P, A, latitude, longitude = bring_data()

# 현재 질문을 추적하는 session_state 변수를 초기화합니다.
if 'current_question_index' not in st.session_state:
    st.session_state.current_question_index = 0

def tourist():
    i = st.session_state.current_question_index
    if i < len(Q):
        if st.button(f'{Q[i]}'):
            st.info(f'{A[i]}')
        if st.button('다음 질문'):
            i += 1
            st.session_state.current_question_index = i

tourist()
