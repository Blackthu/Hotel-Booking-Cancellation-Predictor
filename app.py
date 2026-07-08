import streamlit as st
import subprocess
import sys

st.write(sys.version)

result = subprocess.run(
    [sys.executable, "-m", "pip", "list"],
    capture_output=True,
    text=True
)

st.text(result.stdout)