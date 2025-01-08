import streamlit as st
import random

# 초기화: 눌린 버튼 상태와 배경색 관리
if "hidden_buttons" not in st.session_state:
    st.session_state.hidden_buttons = set()  # 눌린 버튼의 ID를 저장
if "bg_color" not in st.session_state:
    st.session_state.bg_color = "#FFFFFF"  # 초기 배경색 (흰색)

# 배경색 업데이트 함수
def update_background_color():
    # 랜덤 색상을 생성
    st.session_state.bg_color = f"#{random.randint(0, 0xFFFFFF):06x}"

# CSS로 배경색 적용
st.markdown(
    f"""
    <style>
        body {{
            background-color: {st.session_state.bg_color};
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# 제목
st.title("의미없는 버튼들")

# 버튼 ID 목록
button_ids = list(range(1, 11))  # 버튼 ID (1부터 10까지)

# 모든 버튼이 눌린 경우 메시지와 리셋 버튼 표시
if len(st.session_state.hidden_buttons) == len(button_ids):
    st.markdown(
        """
        <div style='text-align: center; margin-top: 200px;'>
            <h1 style='font-size: 60px; color: gray;'>이런 내 버튼들...</h1>
        </div>
        """,
        unsafe_allow_html=True,
    )
    # 리셋 버튼
    if st.button("버튼 돌려주기"):
        st.session_state.hidden_buttons = set()  # 모든 버튼 초기화
else:
    # 랜덤 배치를 위해 컨테이너 생성
    container = st.container()

    # 랜덤 배치 및 버튼 생성
    random.shuffle(button_ids)  # 랜덤 순서로 섞기

    with container:
        for button_id in button_ids:
            if button_id not in st.session_state.hidden_buttons:  # 숨겨진 버튼 제외
                cols = st.columns(random.randint(1, 5))  # 랜덤한 컬럼 개수
                col = random.choice(cols)  # 랜덤한 컬럼 선택
                if col.button(f"버튼 {button_id}"):
                    st.write("그냥 버튼이다 뭐")
                    st.session_state.hidden_buttons.add(button_id)  # 버튼 숨기기
                    update_background_color()  # 배경색 업데이트
