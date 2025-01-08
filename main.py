import streamlit as st
import random

# 초기화: 눌린 버튼 상태를 관리하기 위한 session_state
if "hidden_buttons" not in st.session_state:
    st.session_state.hidden_buttons = set()  # 눌린 버튼의 ID를 저장

# 제목
st.title("의미없는 버튼들")

# 버튼 고정 순서 (1부터 10까지)
button_ids = list(range(1, 11))

# 랜덤 배치를 위해 컨테이너 생성
container = st.container()

# 버튼 생성 및 랜덤 배치
with container:
    for button_id in button_ids:
        if button_id not in st.session_state.hidden_buttons:  # 숨겨진 버튼 제외
            cols = st.columns(random.randint(1, 5))  # 랜덤한 컬럼 개수
            col = random.choice(cols)  # 랜덤한 컬럼 선택
            if col.button(f"버튼 {button_id}"):
                st.write("그냥 버튼이다 뭐")
                st.session_state.hidden_buttons.add(button_id)  # 버튼 숨기기
