import streamlit as st
from pathlib import Path

st.write("Current directory:", Path.cwd())

req = Path("requirements.txt")

st.write("requirements.txt exists:", req.exists())

if req.exists():
    st.code(req.read_text())