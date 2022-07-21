import numpy as np
import pandas as pd
import streamlit as st
from skimage.io import imread


# download the image
img_url = 'https://commons.wikimedia.org/wiki/File:%E5%90%8D%E5%B7%A5%E5%A4%A7(20200122)_03.jpg
im = imread(img_url)

st.image(im, caption='image from wikimedia commons',
         use_column_width=True)


# show histgram of all colors
hist_red, _ = np.histogram(im[:, :, 0], bins=64)
hist_green, _ = np.histogram(im[:, :, 1], bins=64)
hist_blue, _ = np.histogram(im[:, :, 2], bins=64)
hist = np.stack((hist_red, hist_green, hist_blue), axis=1)

df_hist = pd.DataFrame(hist, columns=['R', 'G', 'B'])
st.bar_chart(df_hist)


# choose one color
color = st.radio(
    "choose R, G, or B",
    ('R', 'G', 'B'))
if color == 'R':
    df_hist = pd.DataFrame(hist_red)
    st.bar_chart(df_hist)
if color == 'G':
    df_hist = pd.DataFrame(hist_green)
    st.bar_chart(df_hist)
if color == 'B':
    df_hist = pd.DataFrame(hist_blue)
    st.bar_chart(df_hist)
