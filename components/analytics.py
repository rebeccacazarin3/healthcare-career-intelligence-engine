import plotly.express as px


def salary_by_category(df):
    """
    Creates an interactive bar chart showing the average salary
    for each healthcare career category.
    """

    salary_df = (
        df.groupby("Category", as_index=False)["Median_Salary_USD"]
          .mean()
          .sort_values("Median_Salary_USD", ascending=False)
    )

    fig = px.bar(
        salary_df,
        x="Category",
        y="Median_Salary_USD",
        text_auto=".0f",
        title="Average Salary by Career Category",
        color_discrete_sequence=[
            "#0D1B2A",   # Ink Black
            "#1B263B",   # Prussian Blue
            "#415A77",   # Dusk Blue
            "#778DA9",   # Lavender Grey
            "#E0E1DD"    # Alabaster   
        ]
    )

    fig.update_layout(
        xaxis_title="Career Category",
        yaxis_title="Average Salary (USD)"
    )

    return fig


# Education Distribution by Category

def education_distribution(df):
    education_df = (
        df["Education"]
        .value_counts()
        .reset_index()
    )

    education_df.columns = ["Education", "Count"]

    fig = px.pie(
        education_df,
        names="Education",
        values="Count",
        title="Education Requirements"
    )

    return fig

# AI Relevance Distribution by Category

def ai_relevance_chart(df):

    ai_df = (
        df["AI_Relevance"]
        .value_counts()
        .reset_index()
    )

    ai_df.columns = ["AI_Relevance", "Count"]

    fig = px.bar(
        ai_df,
        x="AI_Relevance",
        y="Count",
        title="AI Relevance of Careers",
        text_auto=True
    )

    return fig