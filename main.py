import streamlit as st
import random

# 제목
st.title("의미없는 버튼들")

# 랜덤한 배치를 위해서 컨테이너와 컬럼을 조합
container = st.container()

# 버튼들을 랜덤 배치
with container:
    for _ in range(10):  # 버튼 10개 생성
        cols = st.columns(random.randint(1, 5))  # 랜덤한 컬럼 개수
        col = random.choice(cols)  # 랜덤한 컬럼 선택
        if col.button(f"버튼 {_+1}"):
            st.write("그냥 버튼이다 뭐")

