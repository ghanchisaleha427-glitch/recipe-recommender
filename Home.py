import streamlit as st
import os

st.set_page_config(page_title="Smart Recipe Recommendation System", layout="wide")

# Absolute path for image
image_path = os.path.join(os.path.dirname(__file__), "P1.jpg")

# Center block with compact spacing
col1, col2, col3 = st.columns([1,2,1])  # middle column wide
with col2:
    # Logo perfectly centered
    st.image(image_path, width=400)   

    # Text block compact and closer to logo
    st.markdown(
        "<h1 style='text-align: center; margin-top:-15px;'>Smart Recipe Recommendation System</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center; margin-top:-10px;'>Welcome to LARANA Bite! Use the sidebar to navigate authentication pages.</p>",
        unsafe_allow_html=True
    )

