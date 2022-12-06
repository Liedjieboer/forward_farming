import streamlit as st
import base64
from wordcloud_gen.wordcloud_year import WordcloudYear

st.set_page_config(
    page_title="Flags to wordclouds",
    page_icon=":cloud:",
    initial_sidebar_state="collapsed"
)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('boudewijn-boer-qT515JdZNy8-unsplash.jpg')

st.markdown("<h1 style='font-size:50px; font-family:didot; text-align: center; color: black;'>Select the year</h1>", unsafe_allow_html=True)

option = st.select_slider('Select the year', [2072, 2122, 2172])
option_dict = {2072:'bad', 2122:'good', 2172:'excellent'}
if option is not None:
    st.write(WordcloudYear.wordcloud_gen(option_dict[option]))
