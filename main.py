import io
import matplotlib
import folium
import random

import streamlit as st
import streamlit.components.v1 as html
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import pandas as pd

import i18n
import style
import assets
import data
import requests
import json

from PIL import Image
from streamlit_folium import st_folium
from streamlit_option_menu import option_menu
from streamlit_js_eval import get_browser_language


# 데이터 프레임을 만들 데이터를 리스트로 정의합니다.
data = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

# 데이터프레임을 생성합니다.
df = pd.DataFrame(data)

# 데이터프레임을 출력합니다.
print(df)



# 스트림릿 앱의 제목을 설정합니다.
st.title("챗봇")

# CSS 스타일을 적용할 HTML 요소를 생성합니다.
style = """
<style>
    /* 여기에 사용자 정의 CSS 스타일을 추가하세요 */
    .custom-button {
        background-color: green;
        color: white;
        font-size: 16px;
        padding: 10px 20px;
        border: none;
        cursor: pointer;
    }

    .custom-button:hover {
        background-color: darkgreen;
    }
</style>
"""

# CSS 스타일을 적용합니다.
st.markdown(style, unsafe_allow_html=True)

# 각 질문에 대한 버튼을 생성하고 버튼이 클릭되면 해당 질문에 대한 답변을 출력합니다.
question_options = list(chatbot.responses.keys())[1:]  # 첫 번째 옵션인 "---질문 선택---"은 제외합니다.

for question in question_options:
    if st.button(question, key=f"button_{question}", help="이 버튼을 클릭하여 질문에 대한 답변을 확인하세요."):
        response = chatbot.get_response(question)
        st.warning(f"'{question}' 라는 질문을 받았습니다.")
        st.success(f"{response}")
