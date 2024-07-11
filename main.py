import streamlit as st

from PIL import Image
from streamlit.elements.image import image_to_url

import FreeSimpleGUI as gui

st.header("Gray Scale Converter")

uploaded_image = st.file_uploader("Upload Image") 
if uploaded_image:
    image=Image.open(uploaded_image)
    gray_image=image.convert("L")
    st.image(gray_image)
    
with st.expander("Start camera"):
    camera_image=st.camera_input("camera")
    

if camera_image:
    img=Image.open(camera_image)

    gray_image=img.convert("L")

    st.image(gray_image)

