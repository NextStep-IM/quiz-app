import streamlit as st

pages = {
    'home': [st.Page('home.py', title='Home')],
    'questions': [st.Page('questions.py', title='Questions')]
}

pg = st.navigation(pages, position='hidden')
pg.run()