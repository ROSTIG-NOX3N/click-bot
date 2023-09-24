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

# 질문과 대답을 정의한 딕셔너리
qa_dict = {
    "안녕": ["안녕하세요!", "안녕하십니까?", "안녕이요!"],
    "오늘 날씨 어때?": ["오늘은 맑아요.", "비가 올 것 같아요.", "날씨는 꽤 괜찮아요."],
    "이름이 뭐야?": ["제 이름은 챗봇이에요.", "저는 챗봇입니다.", "저는 이름이 없어요."],
    "잘 지내니?": ["네, 잘 지내고 있어요.", "그럭저럭 괜찮아요.", "좋은 날이에요."],
    "사용법을 가르쳐줘.": ["물어보고 싶은 질문을 입력하고 엔터 키를 누르세요."],
}

# 챗봇 함수 정의
def chat_with_bot(user_input):
    user_input = user_input.strip()
    if user_input in qa_dict:
        responses = qa_dict[user_input]
        return random.choice(responses)
    else:
        return "그 질문에 대한 대답을 모르겠어요."

# 간단한 챗봇 인터페이스
while True:
    user_input = input("사용자: ")
    if user_input.lower() == "종료":
        print("챗봇: 대화를 종료합니다.")
        break
    response = chat_with_bot(user_input)
    print("챗봇:", response)

