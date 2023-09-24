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
                "해동용궁사를 추천합니다. 해동용궁사를 방문하면 역사와 자연의 아름다움이 어우러진 특별한 경험을 만날 수 있습니다.",
                "해동용궁사를 추천합니다. 해동용궁사는 한국의 불교 역사와 문화를 체험하고 명상과 평화로움을 즐길 수 있는 최고의 장소 중 하나입니다.",
                "해동용궁사를 추천합니다. 해동용궁사는 아름다운 건축물과 자연 경관으로 둘러싸여 있어, 사진 찍기에도 훌륭한 곳입니다",
                "해동용궁사를 추천합니다. 역사와 미를 동시에 즐기고 싶다면 해동용궁사가 더할 나위 없이 좋은 선택입니다.",
                "해운대를 추천합니다. 일몰을 바라보며 해운대 해변을 산책하면 일상의 스트레스를 잊을 수 있는 최적의 힐링 장소입니다.",
                "해운대를 추천합니다. 무엇보다, 해운대는 낮과 밤 모두 활기차고 아름다운 풍경을 선사하여 방문자들에게 특별한 경험을 선사합니다."
            ],
            
            # 맛집 질문과 대답
            "부산에서 가볼만한 맛집에 대해 추천해줘": [
                "해목 해운대점을 추천합니다. 해목 해운대는 유명한 고급식당이고 장어덮밥과 장어와 관련된 식사, 참치, 연어 등 해산물을 주로 다루는 맛집입니다.",
                "선창횟집 해운대점을 추천합니다. 선창횟집은 많은 인원이 외식하기 좋은 곳이고 회 코스요리를 적당한 가격에 바다를 보면서 즐길 수 있습니다.",
                "금수복국 해운대본점을 추천합니다. 금수복국 해운대본점은 복어와 복국을 주로 다루는 맛집이고 사람이 많아도 복잡하지 않고 친절하게 대응하는 서비스가 뛰어난 맛집입니다."
            ],
            
            # 자연/공원 질문과 대답
            "부산에서 가볼만한 자연/공원에 대해 추천해줘": [
                "해운대 해수욕장을 추천합니다. 여름에는 수영, 해변 놀이, 서핑 등 다양한 레저 활동을 즐기기에 최적의 장소이며, 겨울에는 해안을 따라 산책하기에도 좋습니다.",
                "광안리 해수욕장을 추천합니다. 광안대교의 조명은 밤에 특히 아름다우며, 해변가에서 산책하며 로맨틱한 분위기를 느낄 수 있습니다.",
                "UN기념공원을 추천합니다. 공원은 평화와 협력의 가치를 강조하며, 다양한 기념비와 조형물들이 자리하고 있어 역사와 문화를 체험할 수 있습니다."
            ],
            
            # 카페/디저트 질문과 대답
            "부산에서 가볼만한 카페/디저트에 대해 추천해줘": [
                "모모스커피 부산본점을 추천합니다. 주택을 개조한 듯한 카페 인테리어가 인상깊은 감성카페입니다.",
                "에테르 영도점을 추천합니다. 꼭대기 테라스에서 바다를 보면서 먹기 좋을 정도로 뷰가 좋습니다.",
                "초량1941 초량점을 추천합니다. 일본식의 카페라서 이색적인 느낌이 나는 외관을 보유하고 있습니다."
            ],
            
            # 엑스포 질문과 대답
            "부산에 엑스포가 개최될 시 기대효과에 대해 알려줘": [
                "EXPO, 올림픽, 월드컵 등 국제 행사는 그 행사가 개최되는 도시나 국가에 경제적 이익과 홍보 효과를 가져다 줄 수 있습니다.",
                "엑스포 개최는 관광 산업에 큰 활성화를 가져올 것으로 예상됩니다. 부산은 관광명소와 자연 경관으로 유명하므로 엑스포로 더 많은 관광객을 유치할 것으로 기대됩니다.",
                "엑스포 개최는 부산의 이미지와 인지도를 대대적으로 높일 것으로 기대됩니다. 이는 장기적인 관광 산업 발전에 긍정적인 영향을 미칠 것입니다."
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
st.title("부산 안내 챗봇")

# 사용자에게 질문을 입력 받는 컴포넌트를 추가합니다.
question = st.selectbox("질문 선택", list(chatbot.responses.keys()))

# "새로운 질문 생성하기" 버튼을 추가합니다.
if st.button("새로운 질문 생성하기"):
    # 새로운 질문을 생성합니다.
    question = chatbot.get_random_question(question)

# 사용자가 질문을 선택하면 해당 질문에 대한 답변을 출력합니다.
if question != "---질문 선택---":
    response = chatbot.get_response(question)
    st.text("답변:")
    st.write(response)
