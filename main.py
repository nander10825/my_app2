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
    "저 버튼은 그냥 존재한다. 🔘",
    "버튼을 눌러야 알게 되는 사실... 🤫",
    "이 버튼은 신비로워요... ✨",
    "버튼이 없어진다... 어서 눌러봐! ⏳",
    "버튼은 선택이 아닌 필수! 💥",
    "이 버튼이 그 버튼인가? 🕵️‍♂️",
    "버튼을 누르면 비밀이 밝혀져요! 🤐",
    "어쩌면 버튼을 누르면 세상이 바뀔지도... 🌍",
    "버튼을 누를 때마다 운명이 바뀐다! ⚡",
    "버튼 눌러서 뭐가 달라지지 않을까요? 😅",
    "이 버튼을 누르면 또 다른 버튼이 나타날 거예요! 🔄",
    "버튼은 물리학의 법칙을 무시해요. 🔬",
    "버튼을 눌렀다는 사실이 중요해요! ⏺️",
    "버튼의 저항은 항상 0.01Ω! ⚡",
    "버튼을 누르면 난리가 나요! 🚨",
    "버튼은 평범하지 않아요! 🦸‍♂️",
    "버튼을 눌렀다고 모두가 알게 될 거예요! 🎙️",
    "버튼을 누르면 곧 엄청난 일이 일어날 거예요! 🎩",
    "그 버튼을 누르면 새로운 차원이 열려요! 🌌",
    "버튼을 누르면 다른 차원으로 넘어가나요? 👽",
    "버튼을 눌러도 괜찮을까요? 🤔",
    "버튼을 눌렀다고 큰일은 아니겠죠? 😆",
    "이 버튼을 눌렀을 때의 리스크는... 😜",
    "혹시 이 버튼, 타임머신인가요? 🕰️",
    "버튼을 누를 때마다 시간과 공간이 왜곡될 거예요! ⏳",
    "버튼 눌렀다! 이제 무엇이 바뀔까요? 🌟",
    "버튼의 버튼을 누르면 뭔가 변화가 일어날 거예요! 🔄",
    "이 버튼을 누르면 당신의 하루가 달라질 거예요! 🌅",
    "버튼을 누르면 더 많은 버튼이 생길지도? 🔲",
    "혹시 이 버튼이 꿈속에서 나타날까요? 💤",
    "버튼을 누르면 세상의 법칙이 바뀌는 걸까요? 🔮",
    "이 버튼을 누르면 다른 사람에게도 영향을 미칠 거예요! 👫",
    "버튼이 눌렸다고 세상이 조용해지지 않아요! 🔊",
    "버튼을 누른다면, 뭐든지 가능할 거예요! 💡",
    "버튼이 마법의 키일지도 몰라요! 🗝️",
    "버튼을 눌렀다는 것, 중요하지 않나요? 🧐",
    "버튼을 눌러야 답을 알 수 있어요! 🤫",
    "이 버튼을 누르면 비밀이 밝혀져요! 🎉",
    "버튼을 눌렀더니 나의 운명이 바뀌었어요... 🔮",
    "버튼이 이 세상에서 가장 신비로운 것 같아요! 🌀",
    "이 버튼이 누군가의 인생을 바꿀지도 모른다! 🌍",
    "버튼을 눌러도 후회하지 않을 거예요! 💪",
    "메세지는 총 51개! 😲"
]



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
                    # 눌렸을 때 소소한 재미 메시지
                    random_message = random.choice(funny_messages)
                    st.write(random_message)
                    st.session_state.hidden_buttons.add(button_id)  # 버튼 숨기기
