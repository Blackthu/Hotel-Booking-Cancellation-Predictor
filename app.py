import streamlit as st
import hashlib

with open("gb_booking_model.pkl", "rb") as f:
    st.write(hashlib.sha256(f.read()).hexdigest())