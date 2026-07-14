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

# -------------------------------------------------
# Constants
# -------------------------------------------------

education_rank = {
    "Certificate": 1,
    "Associate's": 2,
    "Bachelor's": 3,
    "Master's": 4,
    "Doctorate": 5,
    "PhD": 5
}

ai_rank = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

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

st.markdown("""Explore healthcare career trends through interactive visualizations. Use the sidebar filters to update every chart in real time.""")

# -------------------------------------------------
# KPI Calculations
# -------------------------------------------------

total_careers = len(filtered_df)

average_salary = filtered_df["Median_Salary_USD"].mean()

most_common_education = filtered_df["Education"].mode().iloc[0]

high_ai_careers = len( filtered_df[filtered_df["AI_Relevance"] == "High"])

# -------------------------------------------------
# KPI Display
# -------------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total Careers", total_careers)

with col2:
    st.metric("Average Salary", f"${average_salary:,.0f}")

with col3:
    st.metric("Most Common Education", most_common_education)

with col4:
    st.metric("High AI Careers", high_ai_careers)

# Salary and Education Distribution Charts

salary_chart = salary_by_category(filtered_df)
education_chart = education_distribution(filtered_df)

left, right = st.columns(2)

with left:
    st.subheader("Salary Insights")
    st.plotly_chart(
        salary_chart,
        use_container_width=True
    )

with right:
    st.subheader("Education Trends")
    st.plotly_chart(
        education_chart,
        use_container_width=True
    )

# AI Readiness and Certification Req. Disribution Charts 
left2, right2 = st.columns(2)

with left2:
    st.subheader("AI Readiness")
    st.info("Coming in Version 1.1")
   

with right2:
    st.subheader("Certification Requirements")
    st.info("Coming in Version 1.1")


# Education Distribution by Category

education_chart = education_distribution(filtered_df)


def education_distribution(df):
    education_df = (
        df["Education"]
        .value_counts()
        .reset_index()
    )

st.divider()

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

st.subheader(f"{selected_career}")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Salary",
    f"${career['Median_Salary_USD']:,.0f}"
)

col2.metric(
    "Education",
    career["Education"]
)

col3.metric(
    "AI Relevance",
    career["AI_Relevance"]
)

col4, col5, col6 = st.columns(3)

col4.metric(
    "Job Outlook",
    st.write(career["Job_Outlook"])
)

col5.metric(
    "Python",
    career["Python"]
)

col6.metric(
    "SQL",
    career["SQL"]
)

# -------------------------------------------------
# Career Comparison
# -------------------------------------------------
st.divider()

st.header("⚖️ Career Comparison")

st.caption(
    "Compare two healthcare careers side by side."
)

career_list = sorted(filtered_df["Career"].unique())

if len(career_list) < 2:
    st.warning("Select broader filters to compare two careers.")
else:
    selected_career1 = st.selectbox(
        "Career 1",
        career_list,
        index=0
    )

    selected_career2 = st.selectbox(
        "Career 2",
        career_list,
        index=1
    )

career1 = filtered_df[
    filtered_df["Career"] == selected_career1
].iloc[0]

career2 = filtered_df[
    filtered_df["Career"] == selected_career2
].iloc[0]

# -------------------------------------------------
# Comparison Insights
# -------------------------------------------------

# Salary Comparison

salary1 = career1["Median_Salary_USD"]
salary2 = career2["Median_Salary_USD"]

if salary1 > salary2:

    difference = salary1 - salary2

    st.success(
        f"**{career1['Career']}** earns approximately "
        f"${difference:,.0f} more per year."
    )

elif salary2 > salary1:

    difference = salary2 - salary1

    st.success(
        f"**{career2['Career']}** earns approximately "
        f"${difference:,.0f} more per year."
    )

else:

    st.info(
        "Both careers have the same median salary."
    )

# Education Comparison
edu1 = education_rank[career1["Education"]]
edu2 = education_rank[career2["Education"]]

if edu1 > edu2:
   st.success(
        f"🎓 **{career1['Career']}** requires a "
        f"**{career1['Education']}**, while "
        f"**{career2['Career']}** requires a "
        f"**{career2['Education']}**."
    )
   
elif edu2 > edu1:
    st.success(
        f"🎓 **{career2['Career']}** requires a "
        f"**{career2['Education']}**, while "
        f"**{career1['Career']}** requires a "
        f"**{career1['Education']}**."
    )

else:
    st.info(
        "Both careers have the same education requirements."
    )

# Job Outlook Comparison

job_outlook_scale = {
    "Lower Than Average": 1,
    "Average": 2,
    "Faster than Average": 3,
    "Much Faster Than Average": 4
}

job_outlook1 = job_outlook_scale[career1["Job_Outlook"]]
job_outlook2 = job_outlook_scale[career2["Job_Outlook"]]

if job_outlook1 > job_outlook2:
    st.success(
        f"**{career1['Career']}** has a better job outlook than "
        f"**{career2['Career']}**."
    )
elif job_outlook2 > job_outlook1:
    st.success(
        f"**{career2['Career']}** has a better job outlook than "
        f"**{career1['Career']}**."
    )
else:
    st.info(
        "Both careers have the same job outlook."
    )

# AI Relevance Comparison
ai1 = ai_rank[career1["AI_Relevance"]]
ai2 = ai_rank[career2["AI_Relevance"]]

if ai1 > ai2: 
    st.success(
        f"**{career1['Career']}** is more AI-relevant"
        f"**{career2['Career']}**."
    )

elif ai2 > ai1:
    st.success(
        f"**{career2['Career']}** is more AI-relevant"
        f"**{career1['Career']}**."
    )

else:
    st.info(
        "Both careers have the same AI relevance."
    )

# Python Comparison 

career1["Python"] == career2["Python"]
if career1["Python"] == career2["Python"]:
    st.info(
        "Both careers have the same Python requirements."
    )

elif career1["Python"] == "Yes" and career2["Python"] == "No":
    st.success(
        f"**{career1['Career']}** requires Python skills, "
        f"while **{career2['Career']}** does not."
    )

else:
    st.success(
        f"**{career2['Career']}** requires Python skills, "
        f"while **{career1['Career']}** does not."
    )

# SQL Comparison 

career1["SQL"] == career2["SQL"]
if career1["SQL"] == career2["SQL"]:
    st.info(
        "Both careers have the same SQL requirements."
    )

elif career1["SQL"] == "Yes" and career2["SQL"] == "No":
    st.success(
        f"**{career1['Career']}** requires SQL skills, "
        f"while **{career2['Career']}** does not."
    )

else:
    st.success(
        f"**{career2['Career']}** requires SQL skills, "
        f"while **{career1['Career']}** does not."
    )

with left:

    st.subheader(f"🩺 {career1['Career']}")

    st.write(f"**Salary:** ${career1['Median_Salary_USD']:,.0f}")

    st.write(f"**Education:** {career1['Education']}")

    st.write(f"**Job Outlook:** {career1['Job_Outlook']}")

    st.write(f"**AI Relevance:** {career1['AI_Relevance']}")

    st.write(f"**Python:** {career1['Python']}")

    st.write(f"**SQL:** {career1['SQL']}")
      
with right:

    st.subheader(f"🩺 {career2['Career']}")

    st.write(f"**Salary:** ${career2['Median_Salary_USD']:,.0f}")

    st.write(f"**Education:** {career2['Education']}")

    st.write(f"**Job Outlook:** {career2['Job_Outlook']}")

    st.write(f"**AI Relevance:** {career2['AI_Relevance']}")

    st.write(f"**Python:** {career2['Python']}")

    st.write(f"**SQL:** {career2['SQL']}")

