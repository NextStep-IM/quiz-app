import streamlit as st

st.image('quiz.jpg', use_container_width=True)
st.markdown("<h1 style='text-align: center;'>Welcome to the Civics Quiz!</h1>", unsafe_allow_html=True)
st.text('\n\n')
col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
with col3:
    start_btn = st.button('Start Quiz!')

if start_btn:
    st.switch_page('questions.py')