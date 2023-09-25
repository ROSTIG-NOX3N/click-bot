import streamlit as st
import pandas as pd

df = pd.read_excel("C:/Users/USER/Desktop/data.xlsx")

def tourist_data():
    spots_df = df[df['분류'] == '관광지']
    spots_df = spots_df.reset_index(drop=True)
    Q0 = spots_df['질문']
    P0 = spots_df['장소']
    A0 = spots_df['답변']
    latitude0 = spots_df['위도']
    longitude0 = spots_df['경도']
    return Q0, P0, A0, latitude0, longitude0

def restaurant_data():
    spots_df = df[df['분류'] == '음식점']
    spots_df = spots_df.reset_index(drop=True)
    Q1 = spots_df['질문']
    P1 = spots_df['장소']
    A1 = spots_df['답변']
    latitude1 = spots_df['위도']
    longitude1 = spots_df['경도']
    return Q1, P1, A1, latitude1, longitude1

def nature_data():
    spots_df = df[df['분류'] == '자연/공원']
    spots_df = spots_df.reset_index(drop=True)
    Q2 = spots_df['질문']
    P2 = spots_df['장소']
    A2 = spots_df['답변']
    latitude2 = spots_df['위도']
    longitude2 = spots_df['경도']
    return Q2, P2, A2, latitude2, longitude2

def cafe_data():
    spots_df = df[df['분류'] == '카페/디저트']
    spots_df = spots_df.reset_index(drop=True)
    Q3 = spots_df['질문']
    P3 = spots_df['장소']
    A3 = spots_df['답변']
    latitude3 = spots_df['위도']
    longitude3 = spots_df['경도']
    return Q3, P3, A3, latitude3, longitude3

def expect_data():
    spots_df = df[df['분류'] == '기대효과']
    spots_df = spots_df.reset_index(drop=True)
    Q4 = spots_df['질문']
    P4 = spots_df['장소']
    A4 = spots_df['답변']
    latitude4 = spots_df['위도']
    longitude4 = spots_df['경도']
    return Q4, P4, A4, latitude4, longitude4

def expo_data():
    spots_df = df[df['분류'] == '엑스포']
    spots_df = spots_df.reset_index(drop=True)
    Q5 = spots_df['질문']
    P5 = spots_df['장소']
    A5 = spots_df['답변']
    latitude5 = spots_df['위도']
    longitude5 = spots_df['경도']
    return Q5, P5, A5, latitude5, longitude5


#반복문으로 만들 수 있을것 처럼 보임
Q0, P0, A0, latitude0, longitude0 = tourist_data()
Q1, P1, A1, latitude1, longitude1 = restaurant_data()
Q2, P2, A2, latitude2, longitude2 = nature_data()
Q3, P3, A3, latitude3, longitude3 = cafe_data()
Q4, P4, A4, latitude4, longitude4 = expect_data()
Q5, P5, A5, latitude5, longitude5 = expo_data()



tourist_btn_clicked = st.button(f'{Q0[0]}', key='tourist_btn')
restaurant_btn_clicked = st.button(f'{Q1[0]}', key='restaurant_btn')
nature_btn_clicked = st.button(f'{Q2[0]}', key='nature_btn')
cafe_btn_clicked = st.button(f'{Q3[0]}', key='cafe_btn')
expect_btn_clicked = st.button(f'{Q4[0]}', key='expect_btn')
expo_btn_clicked = st.button(f'{Q5[0]}', key='expo_btn')
expo_next_btn_clicked = st.button('다음 답변', key='expo_next_btn')
expo_back_btn_clicked = st.button('이전 답변', key='expo_back_btn')

i = st.session_state.get('i', 0)
x = st.session_state.get('x', 0)
y = st.session_state.get('y', 0)
latitude = st.session_state.get('latitude', 0)
longitude = st.session_state.get('longitude', 0)



# 관광지 버튼
if tourist_btn_clicked:
    i = 0
    x = P0
    y = A0
    latitude = latitude0
    longitude = longitude0
    st.session_state['i'] = i
    st.session_state['x'] = P0
    st.session_state['y'] = A0
    st.session_state['latitude'] = latitude0
    st.session_state['longitude'] = longitude0
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")
        
# 음식점 버튼
if restaurant_btn_clicked:
    i = 0
    x = P1
    y = A1
    latitude = latitude1
    longitude = longitude1
    st.session_state['x'] = P1
    st.session_state['y'] = A1
    st.session_state['i'] = i
    st.session_state['latitude'] = latitude1
    st.session_state['longitude'] = longitude1
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")
    
# 자연/공원 버튼
if nature_btn_clicked:
    i = 0
    x = P2
    y = A2
    latitude = latitude2
    longitude = longitude2
    st.session_state['x'] = P2
    st.session_state['y'] = A2
    st.session_state['i'] = i
    st.session_state['latitude'] = latitude2
    st.session_state['longitude'] = longitude2
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 카페/디저트 버튼
if cafe_btn_clicked:
    i = 0
    x = P3
    y = A3
    latitude = latitude3
    longitude = longitude3
    st.session_state['x'] = P3
    st.session_state['y'] = A3
    st.session_state['i'] = i
    st.session_state['latitude'] = latitude3
    st.session_state['longitude'] = longitude3
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 기대효과 버튼
if expect_btn_clicked:
    i = 0
    x = P4
    y = A4
    latitude = latitude4
    longitude = longitude4
    st.session_state['x'] = P4
    st.session_state['y'] = A4
    st.session_state['i'] = i
    st.session_state['latitude'] = latitude4
    st.session_state['longitude'] = longitude4
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

# 엑스포 버튼
if expo_btn_clicked:
    i = 0
    x = P5
    y = A5
    latitude= latitude5
    longitude = longitude5
    st.session_state['x'] = P5
    st.session_state['y'] = A5
    st.session_state['i'] = i
    st.session_state['latitude'] = latitude5
    st.session_state['longitude'] = longitude5
    st.success(f"장소: {x[i]}")
    st.info(f"답변: {y[i]}")

    
if expo_next_btn_clicked: #다음 버튼
    if i >= len(x) -1 :
        i = len(x) -1
        st.error('마지막 답변입니다.')
        st.warning('이전 답변 버튼을 클릭해주십시오.')
    else :
        i += 1
        st.session_state['i'] = i
        st.success(f"장소: {x[i]}")
        st.info(f"답변: {y[i]}") 
        
           
if expo_back_btn_clicked: #이전 버튼
    if i <= 0 :
        i = 0
        st.error('처음 답변입니다.')
        st.warning('다음 답변 버튼을 클릭해주십시오.')
    else:
        i -= 1
        st.session_state['i'] = i
        st.success(f"장소: {x[i]}")
        st.info(f"답변: {y[i]}")
 
latitude = st.session_state.get('latitude', [0])
longitude = st.session_state.get('longitude', [0])

latitude_value = latitude[i]
longitude_value = longitude[i]


data = pd.DataFrame({
    'latitude': [latitude_value],
    'longitude': [longitude_value]
})
st.map(data)



