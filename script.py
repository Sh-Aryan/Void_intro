import streamlit as st
import streamlit.components.v1 as components

# Read the HTML file from your repository
with open("your_file.html", "r", encoding="utf-8") as f:
    html_data = f.read()

# Render it
st.title("My Streamlit App")
components.html(html_data, height=500, scrolling=True)
