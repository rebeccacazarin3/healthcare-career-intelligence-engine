def build_career_prompt(
    career,
    average_salary,
    salary_comparison,
    education_level,
    max_education,
    ai_level,
    max_ai
):
    
    return f"""
    Using ONLY the information provided below, generate clear, encouraging, and actionable career guidance.

    --------------------------------------------------
    Career Information
    --------------------------------------------------

    Career:
    {career["Career"]}

    Category:
    {career["Category"]}

    Median Salary:
    ${career["Median_Salary_USD"]:,.0f}

    Education Required:
    {career["Education"]}

    Job Outlook:
    {career["Job_Outlook"]}

    AI Relevance:
    {career["AI_Relevance"]}

    Python Required:
    {career["Python"]}

    SQL Required:
    {career["SQL"]}

    --------------------------------------------------
    Dataset Insights
    --------------------------------------------------

    Average Salary Across Dataset:
    ${average_salary:,.0f}

    Salary Comparison:
    This career's salary is {salary_comparison}.

    Education Requirement Ranking:
    Level {education_level} of {max_education}
    (Current Requirement: {career["Education"]})

    AI Readiness Ranking:
    Level {ai_level} of {max_ai}
    (Current Rating: {career["AI_Relevance"]})

    --------------------------------------------------
    Response Requirements
    --------------------------------------------------

    Use both the Career Information and Dataset Insights to generate your recommendations.

    Interpret the information rather than simply repeating it.

    When appropriate, explain how this career compares with other healthcare careers represented in the dataset.

    Do not invent salary figures, statistics, certifications, or job outlook information that was not provided.

    Keep the tone professional, encouraging, and concise.

    --------------------------------------------------
    Required Sections
    --------------------------------------------------

    ## Career Summary
    Provide a concise overview of the career in two to three sentences.

    ## Salary & Outlook
    Discuss both the salary and the job outlook. Explain what they suggest about long-term career potential.

    ## AI Readiness
    Explain how artificial intelligence is expected to influence this profession and why the AI relevance rating matters.

    ## Skills to Develop
    Provide four to six bullet points.
    Include both:
    - Technical skills
    - Professional (soft) skills
    When applicable, relate each recommendation to this career's AI relevance, education requirements, or technical requirements.

    ## Career Growth Opportunities
    Provide three to five bullet points describing logical next career steps or adjacent healthcare careers.
    Briefly explain why each opportunity is a natural progression.

    ## 90-Day Action Plan
    Provide exactly three actionable recommendations.
    The recommendation should:
    - Begin with a bold action title.
    - Include a one- to two-sentence explanation.
    - Focus on realistic goals someone could accomplish within the next three months.
    
    Do not mention that you are an AI language model.
    Write as if you are an experienced healthcare career advisor speaking directly to the user.
    Avoid generic statements that could apply to every career. Make each section specific to the selected healthcare career.
    """
    