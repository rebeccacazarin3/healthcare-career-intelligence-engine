import streamlit as st
import pandas as pd

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Healthcare Career Intelligence Engine",
    page_icon="🏥",
    layout="wide"
)

# -------------------------------------------------
# Load Data
# -------------------------------------------------
df = pd.read_csv("healthcare_careers.csv")

# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🏥 Healthcare Career Intelligence Engine")

st.markdown("""
### AI-Powered Career Discovery & Analytics

Explore healthcare careers, compare required skills, discover certifications,
and receive AI-powered career recommendations.

---
""")

# -------------------------------------------------
# Quick Statistics
# -------------------------------------------------

total_careers = len(df)

average_salary = df["Median Salary"].mean()

categories = df["Category"].nunique()

col1, col2, col3 = st.columns(3)

col1.metric("Healthcare Careers", total_careers)

col2.metric("Average Salary", f"${average_salary:,.0f}")

col3.metric("Career Categories", categories)

st.divider()

# -------------------------------------------------
# Search
# -------------------------------------------------

search = st.text_input(
    "🔍 Search for a healthcare career",
    placeholder="Example: Healthcare Data Analyst"
)

filtered_df = df

if search:
    filtered_df = df[
        df["Career"].str.contains(search, case=False)
    ]

# -------------------------------------------------
# Display Careers
# -------------------------------------------------

st.subheader("Career Explorer")

st.dataframe(
    filtered_df,
    use_container_width=True
)

from utils.data_loader import load_careers

df = load_careers()


