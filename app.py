import streamlit as st
import sklearn
import joblib
import sys

st.write("Python:", sys.version)
st.write("scikit-learn:", sklearn.__version__)
st.write("joblib:", joblib.__version__)