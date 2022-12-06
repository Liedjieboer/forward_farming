import streamlit as st
import base64
from wordcloud_gen.wordcloud_gen import Wordcloud

st.set_page_config(
    page_title="Flags to wordclouds",
    page_icon=":cloud:",
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

st.markdown("<h1 style='font-size:50px; font-family:didot; text-align: center; color: black;'>Select a country</h1>", unsafe_allow_html=True)

option_dict = {'Italy':'ita', 'Portugal':'por', 'USA':'usa', 'Spain':'spa', 'France':'fra', 'Germany':'ger',
       'Argentina':'arg', 'Chile':'chi', 'Australia':'aus', 'South Africa':'rsa',
       'New Zealand':'nz', 'Israel':'isr', 'Hungary':'hun', 'Greece':'grc', 'Romania':'rom',
       'Canada':'can', 'Turkey':'tur', 'Uruguay':'uru', 'England':'eng', 'Bulgaria':'bul'}

option_lst = ['Italy', 'Portugal', 'USA', 'Spain', 'France', 'Germany',
       'Argentina', 'Chile', 'Australia', 'South Africa',
       'New Zealand', 'Israel', 'Hungary', 'Greece', 'Romania',
       'Canada', 'Turkey', 'Uruguay', 'England', 'Bulgaria']

option = st.selectbox('Select a country', option_lst)
if option is not None:
    st.write(Wordcloud.wordcloud_gen(option_dict[option]))
