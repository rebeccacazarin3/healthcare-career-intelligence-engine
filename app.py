import pandas as pd
import plotly.express as px
import streamlit as st
from components.sidebar import build_sidebar
from constants import ai_rank, education_rank
from prompts import build_career_prompt
from utils.data_loader import load_careers
from utils.gemini_helper import generate_career_advice
from components.analytics import (
    education_distribution,
    salary_by_category,
)

df = load_careers()

filtered_df = build_sidebar(df)





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

df = load_careers()

# Clean column names
df.columns = (
    df.columns
        .str.strip()
        .str.replace(" ", "_")
)

# Convert salary column to numeric
df["Median_Salary_USD"] = (
    df["Median_Salary_USD"]
        .astype(str)
        .str.replace("$", "", regex=False)
        .str.replace(",", "", regex=False)
        .str.strip()
)

df["Median_Salary_USD"] = pd.to_numeric(
    df["Median_Salary_USD"],
    errors="coerce"
)

# ---------------------------------------------
# Sidebar
# ---------------------------------------------

with st.sidebar:
    st.title("🏥 HCIE")

    st.caption(
        "Explore healthcare careers using analytics and artificial intelligence."
    )

    st.markdown("---")

    st.markdown("### Navigation")

    st.page_link("app.py", label="🏠 Home")

    st.markdown("---")

    st.markdown("### Filters")

    category = st.selectbox(
        "Category",
        ["All"] + sorted(df["Category"].unique().tolist())
    )

    education = st.selectbox(
        "Education",
        ["All"] + sorted(df["Education"].unique().tolist())
    )

    ai = st.selectbox(
        "AI Relevance",
        ["All"] + sorted(df["AI_Relevance"].unique().tolist())
    )

    st.markdown("---")

    st.markdown("### Coming Soon")

    st.write("🤖 AI Career Coach")
    st.write("📚 Learning Resources")


# -------------------------------------------------
# Header
# -------------------------------------------------
st.title("🏥 Healthcare Career Intelligence Engine")

st.caption(
    "Helping students and professionals explore healthcare careers through AI, analytics, and data."
)

st.markdown(
    """
### Explore Healthcare Careers Through Data & AI

Whether you're exploring career paths, comparing salaries,
or discovering AI-driven opportunities in healthcare,
this dashboard provides data-driven insights to support
your next career decision.

*Built with Python, Pandas, Streamlit, and Google Gemini.*
"""
)

# -------------------------------------------------
# Quick Insights
# -------------------------------------------------

st.divider()

st.subheader("📊 Quick Overview")
st.caption(
    "An overview of the healthcare careers currently available in the database."
)

total_careers = len(df)

average_salary = df["Median_Salary_USD"].mean()

categories = df["Category"].nunique()

ai_careers = len(
    df[df["AI_Relevance"] == "High"]
)

col1, col2, col3, col4 = st.columns(4)

col1.metric("💼 Careers", total_careers)

col2.metric(
    "💰 Avg Salary",
    f"${average_salary:,.0f}"
)

col3.metric(
    "🏥 Categories",
    categories
)

col4.metric(
    "🤖 AI Careers",
    ai_careers
)



#-------------------------------------------------
# Career Highlights
#-------------------------------------------------
st.header("Career Highlights")

st.caption(
    "Automatically generated insights based on the current filters."
)

# Highest Paying Career
highest_paid = filtered_df.loc[
    filtered_df["Median_Salary_USD"].idxmax()
]

st.success(
    f"**{highest_paid['Career']}** is the highest paying career "
    f"with a median salary of "
    f"${highest_paid['Median_Salary_USD']:,.0f}."
)

# Lowest Paying Career
lowest_paid = filtered_df.loc[
    filtered_df["Median_Salary_USD"].idxmin()
]

st.info(
    f"**{lowest_paid['Career']}** is the lowest paying career "
    f"with a median salary of "
    f"${lowest_paid['Median_Salary_USD']:,.0f}."
)

# Highest Education Required
highest_education = filtered_df.loc[
    filtered_df["Education"].map(education_rank).idxmax()
]

st.success(
    f"**{highest_education['Career']}** requires the highest level of education "
    f"with a requirement of "
    f"**{highest_education['Education']}**."
)


# High AI Careers
high_ai_careers = len(
    filtered_df[
        filtered_df["AI_Relevance"] == "High"
    ]
)

st.success(
    f"**{high_ai_careers}** careers are classified as having **High AI Relevance**."
)

