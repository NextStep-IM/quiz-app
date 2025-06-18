import streamlit as st

pages = {
    'home': [st.Page()],
    'questions': [st.Page()]
}

pg = st.navigation(pages, position='hidden')
pg.run()