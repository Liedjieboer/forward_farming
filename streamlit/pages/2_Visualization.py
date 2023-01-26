import streamlit as st
from PIL import Image

image = Image.open('streamlit/images/colorbar.png')
new_image = image.resize((70,700))

option = st.selectbox(
    'Would you like to see the sites or the change in temperature?',
    ('Sites', 'Temperature'))

if option == 'Sites':
    st.write(
        f"<iframe src='https://cesium.com/ion/stories/viewer/?id=94b064a0-668f-495d-bf86-bdca2364f818' width='1600' height='800'></iframe>",
        unsafe_allow_html=True
    )

elif option == 'Temperature':
    # col1, col2, col3 = st.columns(3)
    # with col1:

    col1, col2 = st.columns([7, 1])
    col1.write(
        f"<iframe src='https://cesium.com/ion/stories/viewer/?id=5fdeb51a-4be7-4231-9f4f-e0c9d77aed12' width='1500' height='800'></iframe>", #width='500' height='400'
        unsafe_allow_html=True
    )
    col2.image(new_image)
