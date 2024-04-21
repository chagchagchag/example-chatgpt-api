import streamlit as st

foods = st.multiselect("다이어트 때 미치는 음식", {"라면", "신라면", "새우깡", "삼겹살", "피자"})

st.write(', '.join(foods))
