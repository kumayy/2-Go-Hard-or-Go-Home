# core pkgs
import streamlit as st

# ----WORKİNG WITH MEDIA FILES-----

# display img
from PIL import Image
img = Image.open("data/image_03.jpg")
st.image(img)
st.image(img, use_column_width=True)

# image from url
st.image("https://i.imgur.com/PnnLSpb.jpeg")

#display video
video_file = open("data/annie spin.mp4","rb").read()
st.video(video_file)

video_file_2 = open("data/cooliovid.mp4","rb").read()
st.video(video_file_2, start_time = 14)

st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

# audio files
audio_file = open("data/gangstaparadise.m4a","rb")
st.audio(audio_file.read())

