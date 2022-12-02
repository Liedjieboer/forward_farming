import streamlit as st
import base64

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

option_dict = {'---':None, 'Italy':'ita', 'Portugal':'por', 'USA':'usa', 'Spain':'spa', 'France':'fra', 'Germany':'ger',
       'Argentina':'arg', 'Chile':'chi', 'Australia':'aus', 'South Africa':'rsa',
       'New Zealand':'nz', 'Israel':'isr', 'Hungary':'hun', 'Greece':'grc', 'Romania':'rom',
       'Canada':'can', 'Turkey':'tur', 'Uruguay':'uru', 'England':'eng', 'Bulgaria':'bul'}

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

flag_wordcloud(option_dict[option])
