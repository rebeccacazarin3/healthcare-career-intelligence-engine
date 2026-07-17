




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

