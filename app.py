import pandas as pd
import streamlit as st
import plotly.express as px 

from utils.data_loader import load_careers
from components.analytics import salary_by_category
from components.analytics import education_distribution


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

# -------------------------------------------------
# Quick Insites
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
# Display Table and Charts
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

# -------------------------------------------------
# Analytics Dashboard
# -------------------------------------------------

st.divider()

st.header("📊 Analytics Dashboard")

st.markdown(
    """
Explore healthcare career trends through interactive visualizations. Use the sidebar filters to update every chart in real time.
"""
)

# Salary and Education Distribution Charts

salary_chart = salary_by_category(filtered_df)
education_chart = education_distribution(filtered_df)

left, right = st.columns(2)

with left:
    st.subheader("💰 Salary Insights")
    st.plotly_chart(
        salary_chart,
        use_container_width=True
    )

with right:
    st.subheader("🎓 Education Trends")
    st.plotly_chart(
        education_chart,
        use_container_width=True
    )

left2, right2 = st.columns(2)

with left2:
    st.subheader("🤖 AI Readiness")
    st.info("Coming in Version 1.1")
   

with right2:
    st.subheader("🏅 Certification Requirements")
    st.info("Coming in Version 1.1")


# Education Distribution by Category

education_chart = education_distribution(filtered_df)


def education_distribution(df):
    education_df = (
        df["Education"]
        .value_counts()
        .reset_index()
    )

# -------------------------------------------------
# Career Profile
# -------------------------------------------------

st.divider()

st.header(" 🩺 Career Profile")

st.caption(
    "Select a healthcare career to view its salary, education, job outlook, and technical requirements."
)

selected_career = st.selectbox(
    "Select a Career",
    sorted(filtered_df["Career"].unique())
)

career = filtered_df[
    filtered_df["Career"] == selected_career
].iloc[0]

if filtered_df.empty:
    st.warning("No careers match your current filters.")


st.subheader(f"🩺 {selected_career}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "💰 Salary",
    f"${career['Median_Salary_USD']:,.0f}"
)

col2.metric(
    "🎓 Education",
    career["Education"]
)

col3.metric(
    "🤖 AI Relevance",
    career["AI_Relevance"]
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "📈 Job Outlook",
    st.write(career["Job_Outlook"])
)

col5.metric(
    "🐍 Python",
    career["Python"]
)

col6.metric(
    "🗄 SQL",
    career["SQL"]
)

