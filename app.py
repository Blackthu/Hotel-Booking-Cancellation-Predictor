import streamlit as st

st.title("Test")

try:
    import joblib
    st.success(f"joblib imported successfully! Version: {joblib.__version__}")
except Exception as e:
    st.exception(e)