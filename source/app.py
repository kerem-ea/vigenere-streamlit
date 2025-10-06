import streamlit as st

st.set_page_config(
   page_title="Vigenere projekt",
   page_icon="",
   layout="wide",
   initial_sidebar_state="expanded",
)

main = st.Page("main.py", title="Hjem")
vigenere = st.Page("vigenere.py", title="Vigenere kryptering") 

pg = st.navigation([main, vigenere])
pg.run() 