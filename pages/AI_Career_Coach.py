









# -------------------------------------------------
# AI Career Coach
# -------------------------------------------------

st.divider()

st.header("🤖 AI Career Coach")

st.caption(
    "Receive AI-powered insights and career guidance based on the selected healthcare career. AI-generated guidance is intended to supplement your career research and should not be considered professional career advice."
)

generate_advice = st.button(
    "Generate AI Career Advice",
    use_container_width=True
)

if generate_advice:

    average_salary = filtered_df["Median_Salary_USD"].mean()

    salary_difference = (
        career["Median_Salary_USD"] - average_salary
    )
    if salary_difference > 0:
        salary_comparison = (
            f"${salary_difference:,.0f} above the dataset average"
        )
    elif salary_difference < 0:
        salary_comparison = (
            f"${abs(salary_difference):,.0f} below the dataset average"
        )
    else:
        salary_comparison = (
            "equal to the dataset average"
        )

    education_level = education_rank[
        career["Education"]
    ]

    max_education = max(
        education_rank.values()
    )

    ai_level = ai_rank[
        career["AI_Relevance"]
    ]

    max_ai = max(ai_rank.values())

    prompt = build_career_prompt(
    career,
    average_salary,
    salary_comparison,
    education_level,
    max_education,
    ai_level,
    max_ai
    )
    
    with st.spinner("Generating personalized career advice..."):
        advice = generate_career_advice(prompt)

    st.markdown(advice)
