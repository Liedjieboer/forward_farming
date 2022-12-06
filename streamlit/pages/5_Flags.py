import streamlit as st
import base64
from PIL import Image
from wordcloud_gen.wordcloud_gen import Wordcloud

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
