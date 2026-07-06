import plotly.express as px

def salary_by_category(df):
    salary_df = (
        df.groupby("Category", as_index=False)["Median_Salary_USD"]
          .mean()
          .sort_values("Median_Salary_USD", ascending=False)
    )

    fig = px.bar(
        salary_df,
        x="Category",
        y="Median_Salary_USD",
        title="Average Salary by Career Category",
        text_auto=".0f"
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Average Salary (USD)"
    )

    return fig