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

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# 관광지

용궁사1 = "해동용궁사를 추천합니다. 해동용궁사를 방문하면 역사와 자연의 아름다움이 어우러진 특별한 경험을 만날 수 있습니다."
용궁사2 = "해동용궁사를 추천합니다. 해동용궁사는 한국의 불교 역사와 문화를 체험하고 명상과 평화로움을 즐길 수 있는 최고의 장소 중 하나입니다."
용궁사3 = "해동용궁사를 추천합니다. 해동용궁사는 아름다운 건축물과 자연 경관으로 둘러싸여 있어, 사진 찍기에도 훌륭한 곳입니다"
용궁사4 = "해동용궁사를 추천합니다. 역사와 미를 동시에 즐기고 싶다면 해동용궁사가 더할 나위 없이 좋은 선택입니다."

해운대1 = "해운대를 추천합니다. 일몰을 바라보며 해운대 해변을 산책하면 일상의 스트레스를 잊을 수 있는 최적의 힐링 장소입니다."
해운대2 = "해운대를 추천합니다. 무엇보다, 해운대는 낮과 밤 모두 활기차고 아름다운 풍경을 선사하여 방문자들에게 특별한 경험을 선사합니다."
해운대3 = "해운대를 추천합니다. 해운대는 국내 최고의 해수욕장 중 하나로, 화사한 모래사장과 푸른 바다가 매력적입니다."

남포동1 = "남포동을 추천합니다. 남포동은 부산의 역사적인 중심지로, 오랜 역사와 현대적인 매력이 어우러진 곳입니다."
남포동2 = "남포동을 추천합니다. 현지 음식을 즐기기 위해 남포동 근처의 식당과 먹거리 거리를 탐험할 수 있습니다."
남포동3 = "남포동을 추천합니다. 이곳에서는 다양한 상점과 시장에서 쇼핑을 즐기며 지역 특산품을 구입할 수 있습니다."

태종대1 = "태종대를 추천합니다. 태종대는 부산의 아름다운 해안에 자리하고 있으며, 푸른 바다와 함께 자연 경관을 감상하기에 최적의 장소입니다."
태종대2 = "태종대를 추천합니다. 역사와 자연의 조화로운 분위기와 아름다운 경관은 방문자들에게 특별한 경험을 선사합니다."

송도해상케이블카1 = "송도해상케이블카를 추천합니다. 특히 일몰 시간에 케이블카를 타면 더욱 멋진 풍경을 만날 수 있으며, 사진을 찍기에도 좋은 장소 중 하나입니다."
송도해상케이블카2 = "송도해상케이블카를 추천합니다. 송도해상케이블카를 타면 자연과 도시의 조화로운 아름다움과 바다의 경치를 경험하며 특별한 추억을 만들 수 있습니다."

감천문화마을1 = "감천문화마을을 추천합니다. 감천문화마을은 부산에 위치한 예술과 문화가 공존하는 공간으로, 독특한 건축물과 예술 작품들이 즐비한 곳입니다."
감천문화마을2 = "감천문화마을을 추천합니다. 이 마을은 전통과 현대가 만나는 곳으로, 고요한 골목길과 예술 작품이 함께 어울려 아름다운 풍경을 제공합니다."

# 맛집

해목1 = "해목 해운대점을 추천합니다. 해목 해운대는 유명한 고급식당이고 장어덮밥과 장어와 관련된 식사, 참치, 연어 등 해산물을 주로 다루는 맛집입니다."

선창횟집1 = "선창횟집 해운대점을 추천합니다. 선창횟집은 많은 인원이 외식하기 좋은 곳이고 회 코스요리를 적당한 가격에 바다를 보면서 즐길 수 있습니다."

금수복국1 = "금수복국 해운대본점을 추천합니다. 금수복국 해운대본점은 복어와 복국을 주로 다루는 맛집이고 사람이 많아도 복잡하지 않고 친절하게 대응하는 서비스가 뛰어난 맛집입니다."

이재모피자1 = "이재모피자 테이크아웃점 부산중구점을 추천합니다. 부산의 유명한 피자 맛집으로 많은 사람들에게 실망시키지 않는 맛으로 많은 사람들에게 추천받는 부산의 맛집중 하나입니다."

할매국밥1 = "60년전통 할매국밥 범일동점을 추천합니다. 부산의 음식을 떠올리라하면 대부분 국밥을 떠올리고 국밥맛집인 60년전통 할매국밥 범일동점을 추천합니다. 만약 처음 먹는다면 최고의 음식점으로 경험하고 싶은분들께 추천합니다."

# 자연/공원

해운대해수욕장1 = "해운대 해수욕장을 추천합니다. 여름에는 수영, 해변 놀이, 서핑 등 다양한 레저 활동을 즐기기에 최적의 장소이며, 겨울에는 해안을 따라 산책하기에도 좋습니다."
해운대해수욕장2 = "해운대 해수욕장을 추천합니다. 해운대 해수욕장 근처에는 다양한 레스토랑, 카페, 상점들이 있어 지역 음식과 쇼핑을 즐길 수 있습니다."
해운대해수욕장3 = "해운대 해수욕장을 추천합니다. 부산의 대표적인 관광지 중 하나로, 교통 접근성이 우수하여 관광객들에게 즐거운 휴가를 제공합니다."

광안리1 = "광안리 해수욕장을 추천합니다. 광안대교의 조명은 밤에 특히 아름다우며, 해변가에서 산책하며 로맨틱한 분위기를 느낄 수 있습니다."
광안리2 = "광안리 해수욕장을 추천합니다. 여름에는 수영, 서핑, 비치발리볼 등 다양한 레저 활동을 즐기며, 겨울에는 해안을 따라 산책하는 것도 좋습니다."

기념공원1 = "UN기념공원을 추천합니다. UN기념공원은 역사적으로 중요한 장소로서 평화와 국제 협력에 대한 의미를 다시 생각해보고 싶을 때 방문하기 좋은 장소입니다."
기념공원2 = "UN기념공원을 추천합니다. 유엔과 평화에 관한 다양한 정보와 전시물이 전시되어 있어, 평화와 국제 협력에 대한 이해를 높일 수 있습니다."
기념공원3 = "UN기념공원을 추천합니다. 공원은 평화와 협력의 가치를 강조하며, 다양한 기념비와 조형물들이 자리하고 있어 역사와 문화를 체험할 수 있습니다."

용두산1 = "용두산 공원을 추천합니다. 용두산 공원은 자연 속에서 휴식을 즐기고자 하는 사람들에게 좋은 장소로, 역사와 자연의 조화로운 아름다움을 느낄 수 있습니다."
용두산2 = "용두산 공원을 추천합니다. 주변에 부산타워가 있고 옆에 남포동이 있어 주변 번화가에 쉽게 접근할 수 있습니다."

송도1 = "송도 해수욕장을 추천합니다. 송도 해수욕장 부근에는 송도 센트럴파크와 다양한 관광 명소가 있어, 해변에서 레저를 즐긴 후에 관광할 곳이 많습니다."
송도2 = "송도 해수욕장을 추천합니다. 부산 송도 해수욕장은 여름 휴가와 해변에서의 휴식을 즐기기에 최적의 목적지 중 하나로, 가족이나 친구와 함께 즐거운 시간을 보낼 수 있습니다."
송도3 = "송도 해수욕장을 추천합니다. 해변이 깨끗하게 관리되어 있어 수영, 썬베드에서 휴식, 비치발리볼, 서핑 등 다양한 해변 활동을 즐기기에 안성맞춤입니다."

이기대1 = "이기대를 추천합니다. 이기대는 가족 나들이, 산책, 피크닉, 사진 찍기, 그리고 자연을 즐기는 활동을 하기에 최적의 장소입니다."
이기대2 =  "이기대를 추천합니다. 오륙도 스카이워크부터 시작해서 이기대를 걷는 해안산책로가 오륙도-농바위-어울마당-이기대-동생말 경로로 4.6km 이어져 있는데 말 그대로 바위 절벽에 구름다리와 울타리로 길을 낸 곳이라 경치가 좋습니다."

# 카페/ 디저트

모모스커피1 = "모모스커피 부산본점을 추천합니다. 주택을 개조한 듯한 카페 인테리어가 인상깊은 감성카페입니다."
모모스커피2 = "모모스커피 부산본점을 추천합니다. 베이커리 종류의 맛이 상당하며 다양한 커피의 풍미가 깊다는 평이 자자합니다."

에테르1 = "에테르 영도점을 추천합니다. 꼭대기 테라스에서 바다를 보면서 먹기 좋을 정도로 뷰가 좋습니다."
에테르2 = "에테르 영도점을 추천합니다. 굉장히 커다란 건물 하나가 전부 카페여서 많은 사람들이 갈 수 있으며 다양한 각도에서 경치를 즐길 수 있습니다."

초량1 = "초량1941 초량점을 추천합니다. 일본식의 카페라서 이색적인 느낌이 나는 외관을 보유하고 있습니다 그로인해 많은 사람들이 찾아가고 대부분의 음료가 우유종류 인것을 생각하고 가셔야 합니다."
초량2 = "초량1941 초량점을 추천합니다. 올라가는길이 힘드니 차량을 통해 이동하지 않는것을 추천하는데 그것을 감안해도 건물의 외관이 굉장히 아름다워 찾아갈만한 곳 입니다."

코랄라니1 = "코랄라니 부산기장점을 추천합니다. 코랄라니는 경관이 최고인 대형 베이커리 카페입니다."
코랄라니2 = "코랄라니 부산기장점을 추천합니다. 코랄라니는 대형 베이커리이고 경관이 굉장히 좋기에 많은 사람을 수용하면서 바다에 위치하여 야외석에서 바다를 보면서 먹기 좋은 카페입니다."

오션브리즈1 = "오션브리즈 청사포점을 추천합니다. 카페가 굉장히 넓어 많은 사람들이 갈 수 있고 바다를 보면서 먹기 좋은 카페입니다."

볼트1 = "Cafe de 220VOLT 영도점을 추천합니다. 카페의 위쪽에서는 영도에서 부산바다와 시내를 내려다 볼 수 있는 매력적인 경관을 가지고 있습니다."
볼트2 = "Cafe de 220VOLT 영도점을 추천합니다. 부산에서 힐링하면서 옥상 루프탑에서 바람을 쐴 수 있을 정도로 멋진 분위기를 가진 카페입니다."

# ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class ChatBot:
    def __init__(self):
        # 질문과 대답을 매핑한 딕셔너리를 초기화합니다.
        self.responses = {
            "---질문 선택---": [
                "질문을 선택하고 답변해주세요"
            ],

            # 관광지 질문과 대답
            "부산에서 가볼만한 관광지에 대해 추천해줘": [
                용궁사1,
                용궁사2,
                용궁사3,
                용궁사4,
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
                볼트1,
                볼트2
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
        st.write(f"{question}라는 질문을 받았습니다.")
        st.success(f"{response}")
