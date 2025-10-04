# source streamlitenv/bin/activate
import streamlit as st

st.set_page_config(page_title="Exoura", page_icon="🪐", layout="wide")
st.subheader("A World Away: Hunting for Exoplanets with AI")
st.write("""
Welcome! This app teaches you the science of **transits** and **false positives**, 
explains how our **AI vetter** works, and lets you **race the model** in a quick game.
""")

# six seven