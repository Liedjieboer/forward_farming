# Loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt

path = "/Users/nico_marais/code/Liedjieboer/forward_farming_big_datasets/winemag-data-130k-v2.csv"

# Load in the dataframe
df = pd.read_csv(path, index_col=0)

# Groupby by country
country = df.groupby("country")

# Create text from description
text = " ".join(review for review in df.description)

# Create stopword list:
stopwords = set(STOPWORDS)
stopwords.update(["drink", "now", "wine", "flavor", "flavors"])

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

countries_dict = {'ita':ita, 'por':por, 'usa':usa, 'spa':spa, 'fra':fra, 'ger':ger,
       'arg':arg, 'chi':chi, 'aus':aus, 'rsa':rsa,
       'nz':nz, 'isr':isr, 'hun':hun, 'grc':grc, 'rom':rom,
       'can':can, 'tur':tur, 'uru':uru, 'eng':eng, 'bul':bul}

# Function to plot wordcloud on flag colours
def flag_wordcloud(country):
    # Generate a word cloud image
    mask = np.array(Image.open(f"/Users/nico_marais/Desktop/flags/flag_{country}.jpg"))
    wordcloud = WordCloud(stopwords=stopwords, background_color="white", mode="RGBA", max_words=1000,
                          mask=mask).generate(countries_dict[country])

    # create coloring from image
    image_colors = ImageColorGenerator(mask)
    plt.figure(figsize=[7,7])
    plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
    plt.axis("off")

    # store to file
#     plt.savefig(f"img/{country}_wine.png", format="png")

    plt.show()
