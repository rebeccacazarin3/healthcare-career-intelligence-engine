import streamlit as st

def build_sidebar(df, show_filters=True):

    with st.sidebar:

        st.title("🏥 HCIE")

        st.caption(
        "Explore healthcare careers using analytics and artificial intelligence."
        )

    if show_filters:

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

    filtered_df = df.copy()

    if show_filters:

        if category != "All":
            filtered_df = filtered_df[
                filtered_df["Category"] == category
            ]

        if education != "All":
            filtered_df = filtered_df[
                filtered_df["Education"] == education
            ]

        if ai != "All":
            filtered_df = filtered_df[
                filtered_df["AI_Relevance"] == ai
            ]

    return filtered_df
