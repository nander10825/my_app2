import streamlit as st
import random

st.title("앱 만들거임")
st.text("\n\n")
st.write(" 난 신이다 🪽")
st.write("내 주소? 알아서 뭐하게!끄져!")

st.button("리셋", type="primary")
if st.button("버튼"):
    st.write("그냥 버튼이다 뭐")
else:
    st.write(" ")

