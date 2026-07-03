import pandas as pd
import streamlit as st

@st.cache_data
def load_careers():
    """Load healthcare career data."""
    return pd.read_csv("data/healthcare_careers.csv")
