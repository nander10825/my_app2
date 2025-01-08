import streamlit as st

st.title("앱 만들거임")
st.text("\n\n")
st.write(" 난 신이다 🪽")
st.write("내 주소? 알아서 뭐하게!끄져!")

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

if st.button("Aloha", type="tertiary"):
    st.write("Ciao")
