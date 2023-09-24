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
        self.responses = {}
        self.last_question = None

    def add_response(self, question, answer):
        self.responses[question] = answer

    def get_response(self, question):
        if question == self.last_question:
            response = random.choice(list(self.responses.values()))
        else:
            response = self.responses.get(question, "그 질문에 대한 답변을 모르겠어요.")
        self.last_question = question
        return response

# 챗봇 인스턴스 생성
chatbot = ChatBot()

# 예제 답변 추가
chatbot.add_response("안녕", "안녕하세요!")
chatbot.add_response("날씨 어때?", "오늘은 맑아요.")
chatbot.add_response("이름이 뭐야?", "저는 챗봇이에요.")

# Streamlit 애플리케이션 정의
def main():
    st.title("버튼 클릭형 챗봇")

    # 사용자 입력 받기
    user_input = st.text_input("사용자 입력:")

    # 버튼 클릭 이벤트 처리
    if st.button("챗봇에게 질문"):
        if user_input:
            # 사용자 입력을 챗봇에 전달하고 응답 받기
            bot_response = chatbot.get_response(user_input)

            # 챗봇 응답 출력
            st.write("챗봇 응답:", bot_response)

if __name__ == "__main__":
    main()

