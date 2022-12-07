# Loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
# from custom_wordcloud import WordCloud, STOPWORDS
import streamlit as st
import time
from wordcloud import WordCloud, STOPWORDS

import matplotlib.pyplot as plt

class WordcloudYear:

    def __init__(self, desc):
        self.desc = desc

    def wordcloud_gen(self):

        # Create stopword list:
        stopwords = set(STOPWORDS)
        stopwords.update('drink', 'now', 'wine', 'flavor', 'flavors',
                          'the', 'it', 'is','now', 'age', 'certain', 'age', "it's", '2028',
                          'cannot', 'through', 'years', 'the')

        def transform_zeros(val):
            if val == 0:
                return 255
            else:
                return val

        mask_2072 = np.array(Image.open('streamlit/images/year_mask_Page_1.png'))
        mask_2122 = np.array(Image.open('streamlit/images/year_mask_Page_2.png'))
        mask_2172 = np.array(Image.open('streamlit/images/year_mask_Page_3.png'))

        maskable_image_1 = np.ndarray((mask_2072.shape[0],mask_2072.shape[1]), np.int32)
        maskable_image_2 = np.ndarray((mask_2122.shape[0],mask_2122.shape[1]), np.int32)
        maskable_image_3 = np.ndarray((mask_2172.shape[0],mask_2172.shape[1]), np.int32)


        for i in range(len(mask_2072)):
            maskable_image_1[i] = list(map(transform_zeros, mask_2072[i]))
        for i in range(len(mask_2122)):
            maskable_image_2[i] = list(map(transform_zeros, mask_2122[i]))
        for i in range(len(mask_2172)):
            maskable_image_3[i] = list(map(transform_zeros, mask_2172[i]))

        # Generate a word cloud image

        excellent = ['generous', 'the', 'ripe', 'the', 'ripe', 'the', 'the', 'the', 'the', 'the', 'juicy', 'the', 'the',
                        'the', 'it', 'the', 'lively', 'is', 'fresh', 'crisp', 'freshness', 'freshness', 'fresh', 'it', 'now', 'freshness', 'ample', 'age',
                        'it', 'balanced', 'age', 'leaving', 'certain', 'age', 'wait', 'lemon', 'lasting', 'finish', 'finish', 'now', "it's", 'more', 'clean',
                        'develop', 'drink','nature', 'drink', 'smells', 'pungent', 'soils', 'will', 'cannot', 'age', 'well', 'through', 'years',
                        'freshness','freshness', 'freshness', 'freshness', 'refreshing', 'it', 'it', 'that', 'now', 'it', 'balanced', 'it', 'drink', 'will', '2018',
                        'the', 'finish', 'age', 'crispness', 'ample', 'long', "it's", 'sure','to', 'develop', 'drink', 'vintage', 'broadness', 'drink', 'now',
                        'through', 'thrills', 'be', 'tocai', 'drink', 'fynbos', 'barbara', 'wines']

        good = ['the', 'generous', 'the', 'ripe', 'the', 'ripe', 'the', 'the', 'that', 'it', 'the', 'taut', 'zingy', 'the',
                'crisp', 'the', 'it', 'the', 'zesty', 'finish', 'is', 'fresh', 'zesty', 'freshness', 'freshness', 'fresh', 'its',
                'the', 'freshness', 'ample', 'age', 'structure', 'balanced', 'age', 'with', 'its', 'aging', 'hold', 'lemon', 'long', 'finish', 'finish', 'you',
                "it's", 'its', 'clean', 'develop', 'drink', '1972', 'drink', 'heels', 'shouldered', 'grape', 'soils', 'smooth', 'proves', 'forefront',
                'well', 'palate', 'at', 'zesty', 'a', 'fresh', 'fresh', 'zesty', 'refreshing', 'citrus—and', 'fresh', 'lively', 'zesty',
                'freshness', 'lemony', 'crisp', 'freshness', 'totally', 'refreshing', 'crisp', 'that', 'focused',
                'that', 'crisp', 'freshness', 'balanced', 'a', 'drink', 'elegance', 'evolving', 'the', 'finish', 'age',
                'frothy', 'long', "it's", 'sure', 'to', 'develop', 'drink', '2017–2027', 'heels', 'drink', 'now',
                'embodies', 'thrills', 'be', 'tocai', 'drink', 'fynbos', 'barbara', 'juicily']

        bad = ["ripe", "the", "that", "it", "the", "taut", "creates", "fresh", "lively", "crisp",
                "the", "zesty", "finish", "is", "fresh", "zesty", "freshness", "freshness", "fresh", "its", "the", "freshness",
                "ample", "age", "structure", "balanced", "age", "with", "its", "aging", "wait", "lemon", "long",
                "finish", "finish", "you", "it's", "its", "to", "develop", "drink", "1972", "drink", "heels",
                "shouldered", "distinctively", "soils", "smooth", "proves", "least", "well", "through", "at", 'crisp', 'citrusy',
                'a', 'fresh', 'lemony', 'citrusy', 'citric', 'citrusy', 'citric', 'zesty', 'freshness',
               'citric', 'slender', 'emphasizes', 'strike', 'zip', 'flowery', 'gardenia', 'lemony', 'the', 'honeysuckle',
               'zestiness', 'fizz', 'honeysuckle', 'fresh', 'light', 'racy', 'freshness', 'lemony', 'crisp', 'freshness',
               'totally', 'refreshing', 'crisp', 'it', 'focused', 'finish', 'that', 'crisp', 'freshness', 'balanced', 'a',
               'drink', 'poise', 'evolving', 'the', 'finish', 'age', 'frothy', 'lovely', 'long', "it's", 'sure', 'to',
               'develop', 'drink', '2017–2027', 'heels', 'drink', 'embodies', 'thrills', 'be', 'tocai', 'drink', 'tilled',
               'barbara', 'juicily']

        font_path = 'streamlit/Didot.ttc'

        def similar_color_func(word=None, font_size=None,
                        position=None, orientation=None,
                        font_path=None, random_state=None):
            h = 4 # 0 - 360
            s = 87 # 0 - 100
            l = random_state.randint(20, 30) # 0 - 100
            return "hsl({}, {}%, {}%)".format(h, s, l)

        if self == 'bad':
            wordcloud = WordCloud(stopwords=stopwords, font_path=font_path,
               mask=mask_2072, background_color="rgb(255, 255, 255)", mode="RGB",
               max_words=2000, max_font_size=256, min_font_size=30, contour_width=5, contour_color='rgb(87, 11, 6)',
               random_state=42, width=mask_2072.shape[1], color_func=similar_color_func,
               height=mask_2072.shape[0]).generate(" ".join(bad))
            wordcloud.to_file("temp.png")

        if self == 'good':
            wordcloud = WordCloud(stopwords=stopwords, font_path=font_path,
               mask=mask_2122, background_color="rgb(255, 255, 255)", mode="RGB",
               max_words=2000, max_font_size=256, min_font_size=30, contour_width=5, contour_color='rgba(87, 11, 6)',
               random_state=42, width=mask_2122.shape[1], color_func=similar_color_func,
               height=mask_2122.shape[0]).generate(" ".join(good))
            wordcloud.to_file("temp.png")

        if self == 'excellent':
            wordcloud = WordCloud(stopwords=stopwords, font_path=font_path,
               mask=mask_2172, background_color="rgb(255, 255, 255)", mode="RGB",
               max_words=2000, max_font_size=256, min_font_size=30, contour_width=5, contour_color='rgb(87, 11, 6)',
               random_state=42, width=mask_2172.shape[1], color_func=similar_color_func,
               height=mask_2172.shape[0]).generate(" ".join(excellent))
            wordcloud.to_file("temp.png")

        # plt.figure(figsize=[10,10])
        # plt.imshow(wordcloud, interpolation="bilinear")
        # plt.axis("off")
        # fig = plt.gcf()
        # st.pyplot(fig)

        # Add a placeholder
        # latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            # latest_iteration.text(f'Iteration {i+1}')
            bar.progress(i + 1)
            time.sleep(0.1)

        st.image("temp.png")



# Extra words for wordcloud (already added to the list):
# excellent = ['freshness','freshness', 'freshness', 'freshness', 'refreshing', 'it',
#                      'it', 'that', 'now', 'it', 'balanced', 'it', 'drink', 'will', '2018',
#                      'the', 'finish', 'age', 'crispness', 'ample', 'long', "it's", 'sure',
#                      'to', 'develop', 'drink', 'vintage', 'broadness', 'drink', 'now',
#                      'through', 'thrills', 'be', 'tocai', 'drink', 'fynbos', 'barbara', 'wines']

#         good = ['zesty', 'a', 'fresh', 'fresh', 'zesty', 'refreshing', 'citrus—and', 'fresh', 'lively', 'zesty',
#                 'freshness', 'lemony', 'crisp', 'freshness', 'totally', 'refreshing', 'crisp', 'that', 'focused',
#                 'that', 'crisp', 'freshness', 'balanced', 'a', 'drink', 'elegance', 'evolving', 'the', 'finish', 'age',
#                 'frothy', 'long', "it's", 'sure', 'to', 'develop', 'drink', '2017–2027', 'heels', 'drink', 'now',
#                 'embodies', 'thrills', 'be', 'tocai', 'drink', 'fynbos', 'barbara', 'juicily']

#         bad = ['crisp', 'citrusy', 'a', 'fresh', 'lemony', 'citrusy', 'citric', 'citrusy', 'citric', 'zesty', 'freshness',
#                'citric', 'slender', 'emphasizes', 'strike', 'zip', 'flowery', 'gardenia', 'lemony', 'the', 'honeysuckle',
#                'zestiness', 'fizz', 'honeysuckle', 'fresh', 'light', 'racy', 'freshness', 'lemony', 'crisp', 'freshness',
#                'totally', 'refreshing', 'crisp', 'it', 'focused', 'finish', 'that', 'crisp', 'freshness', 'balanced', 'a',
#                'drink', 'poise', 'evolving', 'the', 'finish', 'age', 'frothy', 'lovely', 'long', "it's", 'sure', 'to',
#                'develop', 'drink', '2017–2027', 'heels', 'drink', 'embodies', 'thrills', 'be', 'tocai', 'drink', 'tilled',
#                'barbara', 'juicily']
