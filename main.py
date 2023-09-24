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

class ChatBot:
    def __init__(self):
        self.responses = {
            "안녕": "안녕하세요!",
            "날씨 어때?": "오늘은 맑아요.",
            "이름이 뭐야?": "저는 챗봇이에요."
        }

    def get_response(self, question):
        return self.responses.get(question, "그 질문에 대한 답변을 모르겠어요.")

# 챗봇 인스턴스 생성
chatbot = ChatBot()

# Streamlit 애플리케이션 정의
st.title("선택형 챗봇")

# 선택한 질문을 저장할 변수
selected_question = st.empty()

# 질문 선택을 위한 버튼
if selected_question.button("질문 선택"):
    selected_question.selectbox("질문 선택:", list(chatbot.responses.keys()))

# 버튼 클릭 이벤트 처리
if st.button("챗봇에게 질문"):
    question = selected_question.selectbox("질문 선택:", list(chatbot.responses.keys()))
    bot_response = chatbot.get_response(question)

    # 챗봇 응답 출력
    st.write("챗봇 응답:", bot_response)
