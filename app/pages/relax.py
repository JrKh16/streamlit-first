import streamlit as st

st.title("Relax Page")

if st.button("Sea"):
    st.audio("sounds/sea.mp3")

if st.button("Bird"):
    st.audio("sounds/bird.mp3")

