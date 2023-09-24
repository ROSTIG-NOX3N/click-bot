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
        # 질문과 대답을 매핑한 딕셔너리를 초기화합니다.
        self.responses = {
            "---질문 선택---": [
                "질문을 선택하고 답변해주세요"
            ],

            # 관광지 질문과 대답
            "부산에서 가볼만한 관광지에 대해 추천해줘": [
                해동용궁사1,
                해동용궁사2,
                해동용궁사3,
                해동용궁사4,
                해운대1,
                해운대2,
                해운대3,
                남포동1,
                남포동2,
                남포동3,
                태종대1,
                태종대2,
                송도해상케이블카1,
                송도해상케이블카2,
                감천문화마을1,
                감천문화마을2
            ],
            
            # 맛집 질문과 대답
            "부산에서 가볼만한 맛집에 대해 추천해줘": [
                해목1,
                선창횟집1,
                금수복국1,
                이재모피자1,
                할매국밥1
            ],

            # 자연/공원 질문과 대답
            "부산에서 가볼만한 자연/공원에 대해 추천해줘": [
                해운대해수욕장1,
                해운대해수욕장2,
                해운대해수욕장3,
                광안리1,
                광안리2,
                기념공원1,
                기념공원2,
                기념공원3,
                용두산1,
                용두산2,
                송도1,
                송도2,
                송도3,
                이기대1,
                이기대2
            ],

            # 카페/디저트 질문과 대답
            "부산에서 가볼만한 카페/디저트에 대해 추천해줘": [
                모모스커피1,
                모모스커피2,
                에테르1,
                에테르2,
                초량1,
                초량2,
                코랄라니1,
                코랄라니2,
                오션브리즈1,
                VOLT1,
                VOLT2
            ],

            # 엑스포 기대효과 질문과 대답
            "부산에 엑스포가 개최될 시 기대효과에 대해 알려줘": [
                "EXPO, 올림픽, 월드컵 등 국제 행사는 그 행사가 개최되는 도시나 국가에 경제적 이익과 홍보 효과를 가져다 줄 수 있습니다.",
                "스마트 혁신 강국으로서 국가의 위상을 제고할 수 있습니다.",
                "부산을 거점으로 제2경제권 부흥을 통해 국가가 균형을 이루어 발전할 수 있습니다.",
                "예상 관람객을 약 3,480만명이고 약 43조원의 생산을 유발하고, 약 18조원의 부가가치를, 약 50만명이 일자리를 가질 수 있다고 기대를 할 수 있습니다.",
                "많은 외국인들이 엑스포를 관람하러 오기 때문에 관광산업이 거대해져 지역에 큰 활기를 불러올 수 있습니다.",
                "엑스포는 국제 무대에서 도시의 이미지를 높이는데 도움이 되므로, 이를 통해 부산은 세계적으로 더 많은 관심을 받아 긍정적인 평가를 받을 수 있습니다."
            ],

            # 엑스포 질문과 대답
            "엑스포에 대해 알려줘": [
                "엑스포는 국제 박람회를 가리키는 용어로, 다양한 국가와 기업이 과학, 기술, 문화, 경제, 환경 등 다양한 주제를 공유하고 전시하는 국제 행사를 말합니다.",
                "엑스포는 특정 주제 혹은 주제에 기반되어 개최되고 대부분 그 해의 글로벌 이슈와 관련이 있어 참가자들은 해당 주제에 대한 해결책과 혁신적인 아이디어를 제시합니다.",
                "엑스포는 대규모 전시관과 공연장을 포함해 참가 국가들은 자국의 다양한 작품을 전시하고 다양한 문화 행사와 공연을 개최합니다.",
                "엑스포는 지속 가능한 발전과 환경 보호와 관련된 주제를 다루고 환경 친화적인 기술과 사회적 책임에 대한 논의가 이루어지며, 환경 보호 의식을 증진시킬 수 있습니다.",
                "엑스포는 혁신과 기술 개발을 촉진하는 플랫폼으로 활용되고 참가 국가들은 자국의 과학과 기술 분야의 발전을 선보여 혁신적인 솔루션을 제공합니다."
            ]
        }

    
    def get_random_question(self, current_question):
        # 현재 질문을 제외하고 랜덤하게 질문을 선택합니다.
        question_list = list(self.responses.keys())
        question_list.remove(current_question)
        return random.choice(question_list)
    
    def get_response(self, question):
        # 질문에 해당하는 대답을 랜덤하게 선택합니다.
        if question in self.responses:
            answers = self.responses[question]
            return random.choice(answers)
        else:
            return "죄송해요. 제가 대답할 수 있는 내용이 아닙니다."

# ChatBot 인스턴스를 생성합니다.
chatbot = ChatBot()

# 스트림릿 앱의 제목을 설정합니다.
st.title("챗봇")

# 각 질문에 대한 버튼을 생성하고 버튼이 클릭되면 해당 질문에 대한 답변을 출력합니다.
question_options = list(chatbot.responses.keys())[1:]  # 첫 번째 옵션인 "---질문 선택---"은 제외합니다.

for question in question_options:
    if st.button(question):
        response = chatbot.get_response(question)
        st.write(f"{question}라는 질문을 받았습니다.")
        st.write(f"{response}")
