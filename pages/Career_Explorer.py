import streamlit as st

from components.sidebar import build_sidebar
from utils.data_loader import load_careers
from utils.data_loader import load_careers

st.title("Career Explorer")

df = load_careers()

filtered_df = build_sidebar(df)

st.write(filtered_df.head())

# -------------------------------------------------
# Career explorer
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
