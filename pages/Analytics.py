
df = load_careers()

filtered_df = build_sidebar(df)

salary_by_category(filtered_df)

education_distribution(filtered_df)

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