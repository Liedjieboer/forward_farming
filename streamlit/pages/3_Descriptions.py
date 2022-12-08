import streamlit as st
import time
from wordcloud_gen.wordcloud_year import WordcloudYear

st.set_page_config(
    page_title="Descriptions",
    page_icon=":speak_no_evil:",
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

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>What will our wine taste like?</h1>", unsafe_allow_html=True)
WordcloudYear.wordcloud_gen('bad')
WordcloudYear.wordcloud_gen('good')
WordcloudYear.wordcloud_gen('excellent')

option = st.select_slider('', [2072, 2122, 2172])
option_dict = {2072:'bad', 2122:'good', 2172:'excellent'}
if option is not None:
    if option == 2072:
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            # latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.image("temp_bad.png", width=15)
    elif option == 2122:
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            # latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.image("temp_good.png", width=15)
    elif option == 2172:
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            # latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.image("temp_excellent.png", width=15)
