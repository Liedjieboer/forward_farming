import streamlit as st

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

st.markdown("<h1 style='font-size:80px; font-family:courier new; text-align: center; color: white;'>Forward Farming</h1>", unsafe_allow_html=True)

# st.write("# :tractor: Welcome to Forward Farming! :tractor:")

from PIL import Image
image = Image.open('/Users/nico_marais/code/Liedjieboer/forward_farming_big_datasets/pics/boudewijn-boer-qT515JdZNy8-unsplash.jpg')

st.image(image)

st.markdown(
"""<h1 style='font-size:30px;
font-family:courier new;
text-align: center;
color: white;
'>When will Sheffield have its day in the sun?</h1>"""
, unsafe_allow_html=True)
