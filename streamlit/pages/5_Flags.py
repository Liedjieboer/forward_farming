import streamlit as st
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
import base64
import numpy as np


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

st.markdown("<h1 style='font-size:70px; font-family:didot; text-align: center; color: black;'>Flags To Wordclouds</h1>", unsafe_allow_html=True)

option = st.selectbox(
    'Which wine producing country would you like to see?',
    ('---', 'Italy', 'Portugal', 'USA', 'Spain', 'France', 'Germany', 'Argentina', 'Chile', 'Australia',
     'South Africa', 'New Zealand', 'Israel', 'Hungary', 'Greece', 'Romania', 'Canada', 'Turkey',
     'Uruguay', 'England', 'Bulgaria'))

st.write('You selected:', option)

# Join all reviews of each country:
usa = " ".join(review for review in df[df["country"]=="US"].description)
fra = " ".join(review for review in df[df["country"]=="France"].description)
ita = " ".join(review for review in df[df["country"]=="Italy"].description)
spa = " ".join(review for review in df[df["country"]=="Spain"].description)
por = " ".join(review for review in df[df["country"]=="Portugal"].description)
chi = " ".join(review for review in df[df["country"]=="Chile"].description)
arg = " ".join(review for review in df[df["country"]=="Argentina"].description)
aus = " ".join(review for review in df[df["country"]=="Australia"].description)
ger = " ".join(review for review in df[df["country"]=="Germany"].description)
nz = " ".join(review for review in df[df["country"]=="New Zealand"].description)
rsa = " ".join(review for review in df[df["country"]=="South Africa"].description)
isr = " ".join(review for review in df[df["country"]=="Israel"].description)
grc = " ".join(review for review in df[df["country"]=="Greece"].description)
can = " ".join(review for review in df[df["country"]=="Canada"].description)
hun = " ".join(review for review in df[df["country"]=="Hungary"].description)
bul = " ".join(review for review in df[df["country"]=="Bulgaria"].description)
rom = " ".join(review for review in df[df["country"]=="Romania"].description)
uru = " ".join(review for review in df[df["country"]=="Uruguay"].description)
tur = " ".join(review for review in df[df["country"]=="Turkey"].description)
eng = " ".join(review for review in df[df["country"]=="England"].description)

option_dict = {'---':None, 'Italy':'ita', 'Portugal':'por', 'USA':'usa', 'Spain':'spa', 'France':'fra', 'Germany':'ger',
       'Argentina':'arg', 'Chile':'chi', 'Australia':'aus', 'South Africa':'rsa',
       'New Zealand':'nz', 'Israel':'isr', 'Hungary':'hun', 'Greece':'grc', 'Romania':'rom',
       'Canada':'can', 'Turkey':'tur', 'Uruguay':'uru', 'England':'eng', 'Bulgaria':'bul'}

countries_dict = {'ita':ita, 'por':por, 'usa':usa, 'spa':spa, 'fra':fra, 'ger':ger,
       'arg':arg, 'chi':chi, 'aus':aus, 'rsa':rsa,
       'nz':nz, 'isr':isr, 'hun':hun, 'grc':grc, 'rom':rom,
       'can':can, 'tur':tur, 'uru':uru, 'eng':eng, 'bul':bul}

# Function to plot wordcloud on flag colours
def flag_wordcloud(country):
    # Generate a word cloud image
    mask = np.array(Image.open(f"/Users/nico_marais/Desktop/flags/flag_{country}.jpg"))
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=1000,
                          mask=mask, contour_width=3, contour_color='firebrick').generate(countries_dict[country])

    # create coloring from image
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[7,7])
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")

    # store to file
#     plt.savefig(f"img/{country}_wine.png", format="png")

    plt.show()

st.write(flag_wordcloud(option_dict[option]))
