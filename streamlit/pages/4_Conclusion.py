import streamlit as st
import base64

st.set_page_config(
    page_title="Conclusion",
    page_icon=":wave:",
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

st.markdown("<h2 style='font-size:50px; font-family:didot; \
    text-align: center; color: black;'\
        >There are far better things ahead than any we leave behind.</h2>", unsafe_allow_html=True)

st.markdown("<h2 style='font-size:50px; font-family:didot; text-align: center;\
    font-style:italic; color: black;'> ~ C.S. Lewis ~</h2>", unsafe_allow_html=True)
