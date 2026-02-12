import streamlit as st
import streamlit.components.v1 as components
import os

file_path = "your_file.html" # Double-check this filename!

if os.path.exists(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.success(f"Found {file_path}!")
    components.html(html_content, height=600, scrolling=True)
else:
    st.error(f"Could not find '{file_path}'.")
    st.write("Files currently in your folder:", os.listdir("."))
