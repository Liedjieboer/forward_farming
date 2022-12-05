# Loading all necessary libraries
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import streamlit as st

import matplotlib.pyplot as plt

class WordcloudYear:

    def __init__(self, desc):
        self.desc = desc

    def wordcloud_gen(self):

        # Create stopword list:
        stopwords = set(STOPWORDS)
        stopwords.update('drink', 'now', 'wine', 'flavor', 'flavors',
                          'the', 'it', 'is','now', 'age', 'certain', 'age', "it's", '2028',
                          'cannot', 'through', 'years')

        def transform_zeros(val):
            if val == 0:
                return 255
            else:
                return val

        mask_2072 = np.array(Image.open('/Users/nico_marais/code/Liedjieboer/forward_farming/wordcloud_masks/year_mask_Page_1.png'))
        mask_2122 = np.array(Image.open('/Users/nico_marais/code/Liedjieboer/forward_farming/wordcloud_masks/year_mask_Page_2.png'))
        mask_2172 = np.array(Image.open('/Users/nico_marais/code/Liedjieboer/forward_farming/wordcloud_masks/year_mask_Page_3.png'))

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

        excellent = ['the', 'generous', 'the', 'ripe', 'the', 'ripe', 'the', 'the', 'the', 'the', 'the', 'juicy', 'the', 'the',
                        'the', 'it', 'the', 'lively', 'is', 'fresh', 'crisp', 'freshness', 'freshness', 'fresh', 'it', 'now', 'freshness', 'ample', 'age',
                        'it', 'balanced', 'age', 'leaving', 'certain', 'age', 'wait', 'lemon', 'lasting', 'finish', 'finish', 'now', "it's", 'more', 'clean',
                        'develop', 'drink','nature', 'drink', '2028', 'smells', 'pungent', 'soils', 'will', 'cannot', 'age', 'well', 'through', 'years']

        good = ['the', 'generous', 'the', 'ripe', 'the', 'ripe', 'the', 'the', 'that', 'it', 'the', 'taut', 'zingy', 'the',
                'crisp', 'the', 'it', 'the', 'zesty', 'finish', 'is', 'fresh', 'zesty', 'freshness', 'freshness', 'fresh', 'its',
                'the', 'freshness', 'ample', 'age', 'structure', 'balanced', 'age', 'with', 'its', 'aging', 'hold', 'lemon', 'long', 'finish', 'finish', 'you',
                "it's", 'its', 'clean', 'develop', 'drink', '1972', 'drink', 'heels', 'shouldered', 'grape', 'soils', 'smooth', 'proves', 'forefront',
                'well', 'palate', 'at']

        bad = ['ripe', 'the', 'that', 'it', 'the', 'taut', 'creates', 'fresh', 'lively', 'crisp',
                'the', 'zesty', 'finish', 'is', 'fresh', 'zesty', 'freshness', 'freshness', 'fresh', 'its', 'the', 'freshness',
                'ample', 'age', 'structure', 'balanced', 'age', 'with', 'its', 'aging', 'wait', 'lemon', 'long',
                'finish', 'finish', 'you', "it's", 'its', 'to', 'develop', 'drink', '1972', 'drink', 'heels',
                'shouldered', 'distinctively', 'soils', 'smooth', 'proves', 'least', 'well', 'through','at']

        font_path = '/System/Library/Fonts/Didot.ttc'

        if self == 'bad':
            wordcloud = WordCloud(stopwords=STOPWORDS, font_path=font_path,
               mask=mask_2072, background_color="white",
               max_words=2000, max_font_size=256, contour_width=3, contour_color='firebrick',
               random_state=42, width=mask_2072.shape[1],
               height=mask_2072.shape[0]).generate(str(bad))

        if self == 'good':
            wordcloud = WordCloud(stopwords=STOPWORDS, font_path=font_path,
               mask=mask_2122, background_color="white",
               max_words=2000, max_font_size=256, contour_width=3, contour_color='firebrick',
               random_state=42, width=mask_2122.shape[1],
               height=mask_2122.shape[0]).generate(str(good))

        if self == 'excellent':
            wordcloud = WordCloud(stopwords=STOPWORDS, font_path=font_path,
               mask=mask_2172, background_color="white",
               max_words=2000, max_font_size=256, contour_width=3, contour_color='firebrick',
               random_state=42, width=mask_2172.shape[1],
               height=mask_2172.shape[0]).generate(str(excellent))

        plt.figure(figsize=[7,7])
        plt.imshow(wordcloud, interpolation="bilinear")
        plt.axis("off")
        fig = plt.gcf()
        st.pyplot(fig)
