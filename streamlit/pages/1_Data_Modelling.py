import streamlit as st
import base64

st.set_page_config(
    page_title="Modelling",
    page_icon=":bar_chart:",
    initial_sidebar_state="collapsed"
)

st.markdown(
f"""
<style>
.stApp {{
    background-image: url("https://raw.githubusercontent.com/Liedjieboer/forward_farming/master/streamlit/images/vineyard.jpg");
    background-size: cover
}}
</style>
""",
unsafe_allow_html=True
)

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>What we did</h1>", unsafe_allow_html=True)

# st.markdown("<h3 style='font-size:70px;\
#     font-family:didot; text-align: center;\
#         color: black;'>What we did</h3>", unsafe_allow_html=True)

option = st.selectbox('', ('Minimum', 'Maximum', 'GDD Prediction'))

st.write(option)

if option == 'Minimum':
    st.image('streamlit/images/mins.png')
elif option == 'Maximum':
    st.image('streamlit/images/maxs.png')
else:
    st.image('streamlit/images/gdd.png')
