import pandas as pd
import streamlit as st
import plotly.express as px 
from utils.data_loader import load_careers
from components.analytics import salary_by_category

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

# Debuging 



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
    st.write("📊 Analytics Dashboard")
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

st.divider()
# -------------------------------------------------
# Quick Insites
# -------------------------------------------------

st.divider()

st.subheader("📊 Quick Insights")
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

# -------------------------------------------------
# Search
# -------------------------------------------------
st.divider()

st.subheader("🔍 Career Search")

st.caption(
    "Search by career title or use the filters in the sidebar to narrow your results."
)

search = st.text_input(
    "Career Title",
    placeholder="Example: Clinical Data Analyst"
)

filtered_df = df

if search:
    filtered_df = df[
        df["Career"].str.contains(search, case=False)
    ]


# -------------------------------------------------
# Display Table and Results
# -------------------------------------------------

st.divider()

st.subheader("📋 Career Explorer")

st.caption(
    f"{len(filtered_df)} healthcare careers match."
)

display_df = filtered_df.copy()

display_df["Median_Salary_USD"] = display_df[
    "Median_Salary_USD"
].map("${:,.0f}".format)

st.dataframe(
    display_df[
        [
            "Career",
            "Category",
            "Median_Salary_USD",
            "Education",
            "Job_Outlook",
            "AI_Relevance"
        ]
    ],
    use_container_width=True
)

st.divider()

st.subheader("📊 Analytics Dashboard")

st.caption(
    "Visualize salary trends across healthcare career categories."
)

salary_chart = salary_by_category(filtered_df)

st.plotly_chart(
    salary_chart,
    use_container_width=True
)

