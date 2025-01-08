import streamlit as st
import random

# 초기화: 눌린 버튼 상태를 관리하기 위한 session_state
if "hidden_buttons" not in st.session_state:
    st.session_state.hidden_buttons = set()  # 눌린 버튼의 ID를 저장

# 재미있는 메시지 목록
funny_messages = [
    "왜 누르시죠? 😂",
    "버튼 눌렀다! 🎉",
    "그냥 버튼이다 뭐 🤷‍♂️",
    "어디서 본 것 같지만... 👀",
    "버튼이 줄어들고 있어... 😢",
    "이 버튼은 아주 특별해! 😎",
    "그거 아세요? 버튼의 위치는 계속 변해요! 👍",
    "무언가 미묘하게 변했나요? 👀",
]

# 제목
st.title("의미없는 버튼들")

# 버튼 ID 목록
button_ids = list(range(1, 11))  # 버튼 ID (1부터 10까지)

# 애니메이션 효과를 위한 HTML 코드 추가 (버튼이 클릭될 때 버튼이 "흔들리는" 효과)
def shake_animation(button_id):
    return f"""
    <style>
        #button{button_id} {{
            animation: shake 0.5s ease-in-out;
        }}
        @keyframes shake {{
            0% {{ transform: translateX(0); }}
            25% {{ transform: translateX(-10px); }}
            50% {{ transform: translateX(10px); }}
            75% {{ transform: translateX(-10px); }}
            100% {{ transform: translateX(0); }}
        }}
    </style>
    """

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
        st.experimental_rerun()  # 페이지 새로고침
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
                # 애니메이션을 포함한 버튼 HTML
                button_html = f'<button id="button{button_id}" class="stButton" style="width: 100px; height: 50px;">버튼 {button_id}</button>'
                st.markdown(shake_animation(button_id), unsafe_allow_html=True)
                
                if col.markdown(button_html, unsafe_allow_html=True):
                    # 눌렸을 때 소소한 재미 메시지
                    random_message = random.choice(funny_messages)
                    st.write(random_message)
                    st.session_state.hidden_buttons.add(button_id)  # 버튼 숨기기
