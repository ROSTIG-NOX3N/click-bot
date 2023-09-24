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

import streamlit as st
import random

class ChatBot:
    def __init__(self):
        self.responses = {
            "---질문 선택---" : "질문을 선택하고 답변해주세요" ,
            "부산에서 가볼만한 관광지에 대해 추천해줘": 
            "해동용궁사", 
            "해운대",
            "남포동",
            "태종대",
            "송도해상케이블카",
            "감천문화마을"
            "부산에서 가볼만한 맛집에 대해 추천해줘": 
            "해목 해운대점",
            "선창횟집 해운대점",
            "금수복국 해운대본점",
            "이재모피자 테이크아웃점 부산중구점",
            "60년전통 할매국밥 범일동",
            "부산에서 가볼만한 자연/공원에 대해 추천해줘": 
            "해운대 해수욕장",
            "광안리 해수욕장",
            "UN기념공원",
            "용두산 공원",
            "송도 해수욕장",
            "이기대"
            "부산에서 가볼만한 카페/디저트에 대해 추천해줘":
            "모모스커피 부산본점",
            "에테르 영도점",
            "초량1941 초량점",
            "코랄라니 부산기장점",
            "오션브리즈 청사포",
            "Cafe de 200VOLT 영도점"
            "부산에 엑스포가 개최될 시 기대효과에 대해 알려줘":
            "EXPO, 올림픽, 월드컵 총3가지의 메가이벤트를 개최하는 세계 7번째 국가가 될 수 있습니다.",
            "스마트 혁신 강국으로서 국가의 위상을 제고할 수 있습니다.",
            "부산을 거점으로 제2경제권 부흥을 통해 국가가 균형을 이루어 발전할 수 있습니다.",
            "예상관람객을 약 3,480만명이고 약 43조원의 생산을 유발하고, 약 18조원의 부가가치를, 약 50만명이 일자리를 가질 수 있다고 기대를 할 수 있습니다.",
            "많은 외국인들이 엑스포를 관람하러 오기 때문에 관광산업이 거대해져 지역에 큰 활기를 불러올 수 있습니다.",
            "엑스포는 국제 무대에서 도시의 이미지를 높이는데 도움이 되므로, 이를통해 부산은 세계적으로 더 많은 관심을 받아 긍정적인 평가를 받을 수 있습니다."
            "엑스포에 대해 알려줘":
            "엑스포는 국제 박람회를 가리키는 용어로, 다양한 국가와 기업이 과학, 기술, 문화, 경제, 환경 등 다양한 주제를 공유하고 전시하는 국제 행사를 말합니다.",
            "엑스포는 특정 주제 혹은 주제에 기반되어 개최되고 대부분 그 해의 글로벌 이슈와 관련이 있어 참가자들은 해당 주제에 대한 해결책과 혁신적인 아이디어를 제시합니다.",
            "엑스포는 대규모 전시관과 공연장을 포함해 참가 국가들은 자국의 다양한 작품을 전시하고 다양한 문화 행사와 공연을 개최합니다.",
            "엑스포는 지속 가능한 발전과 환경 보호와 관련된 주제를 다루고 환경 친화적인 기술과 사회적 책임에 대한 논의가 이루어지며, 환경 보호 의식을 증진시킬 수 있습니다.",
            "엑스포는 혁신과 기술 개발을 촉진하는 플랫폼으로 활용되고 참가 국가들은 자국의 과학과 기술 분야의 발전을 선보여 혁신적인 솔루션을 제공합니다."
        }

    def get_response(self, question):
        return self.responses.get(question, "그 질문에 대한 답변을 모르겠어요.")

# 챗봇 인스턴스 생성
chatbot = ChatBot()

# Streamlit 애플리케이션 정의
st.title("부산 2030 월드엑스포를 물어보세요!")
st.markdown("[Expo Link](https://www.expo2030busan.kr/index.do)")

# 질문 선택을 위한 버튼
selected_question = st.selectbox("질문 선택:", list(chatbot.responses.keys()))

# 버튼 클릭 이벤트 처리
if st.button("챗봇에게 질문"):
    bot_response = chatbot.get_response(selected_question)

    # 챗봇 응답 출력
    st.write("챗봇 응답:", bot_response)
