import streamlit as st
import base64

st.set_page_config(
    page_title="Forward Farming",
    page_icon=":tractor:",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown(
f"""
<style>
.stApp {{
    background-image: url(https://raw.githubusercontent.com/Liedjieboer/forward_farming/master/streamlit/vineyard.jpg);
    background-size: cover
}}
</style>
""",
unsafe_allow_html=True
)

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>Forward Farming</h1>", unsafe_allow_html=True)

st.markdown(
"""<h1 style='font-size:25px;
font-family:zapfino;
text-align: center;
color: brown;
'>When will Sheffield have its day in the sun?</h1>"""
, unsafe_allow_html=True)

st.markdown(
"""<h1 style='font-size:25px;
font-family:didot;
text-align: center;
color: black;
'>The effect of climate change on viticulture in Sheffield, UK</h1>"""
, unsafe_allow_html=True)
