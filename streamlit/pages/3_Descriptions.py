import streamlit as st
import base64
from wordcloud_gen.wordcloud_year import WordcloudYear

st.set_page_config(
    page_title="Flags to wordclouds",
    page_icon=":cloud:",
    initial_sidebar_state="collapsed"
)

st.markdown(
f"""
<style>
.stApp {{
    background-image: url(https://raw.githubusercontent.com/Liedjieboer/forward_farming/master/streamlit/images/vineyard.jpg);
    background-size: cover
}}
</style>
""",
unsafe_allow_html=True
)

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>Select the year</h1>", unsafe_allow_html=True)

option = st.select_slider('', [2072, 2122, 2172])
option_dict = {2072:'bad', 2122:'good', 2172:'excellent'}
if option is not None:
    st.write(WordcloudYear.wordcloud_gen(option_dict[option]))
