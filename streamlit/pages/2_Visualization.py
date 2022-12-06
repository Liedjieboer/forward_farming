import streamlit as st
import base64

st.set_page_config(
    page_title="Modelling",
    page_icon=":technologist:",
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

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>Okay, but where?</h1>", unsafe_allow_html=True)

######################################################
### Feel free to change everything below this line ###
######################################################

