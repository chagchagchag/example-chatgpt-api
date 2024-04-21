import streamlit as st

text = st.text_input("이메일을 입력해주세요")
st.write(text)

agreeFlag = st.checkbox("개인정보 수집 동의")
if agreeFlag:
    st.success("동의합니다.")
