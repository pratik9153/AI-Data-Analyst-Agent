import os
import streamlit as st
import pandas as pd

from data_processing.loader import load_data
from data_processing.validator import validate_data
from data_processing.profiler import profile_data

from agents.analyst_agent import (
    understand_question,
    generate_answer
)

from tools.statistics import (
    calculate_statistics,
    calculate_correlation
)

from tools.data_analysis import (
    column_summary,
    group_analysis,
    top_categories
)

from tools.visualization import (
    histogram,
    bar_chart,
    scatter_plot
)


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="AI Data Analyst",
    page_icon="🤖",
    layout="wide"
)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    .main-title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        color: #666;
        margin-bottom: 25px;
    }

    .feature-box {
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #ddd;
        margin-bottom: 10px;
    }

    .insight-box {
        padding: 18px;
        border-radius: 10px;
        border: 1px solid #ddd;
        margin-top: 10px;
    }

    .insight-title {
        font-size: 18px;
        font-weight: 600;
    }

    .insight-text {
        margin-top: 6px;
        font-size: 16px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.markdown(
    '<div class="main-title">🤖 AI Data Analyst</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    Upload your CSV, explore your data, create visualizations,
    and ask questions using an AI-powered data analyst.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# FILE UPLOAD
# =========================================================

uploaded_file = st.file_uploader(
    "📂 Upload your CSV file",
    type=["csv"],
    help="Upload a CSV file up to 200MB."
)

st.caption("200MB per file • CSV")


# =========================================================
# HOME PAGE
# =========================================================

if uploaded_file is None:

    st.markdown("## ✨ What you can do")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.markdown(
            """
            <div class="feature-box">

            <h3>📊 Explore Data</h3>

            <p>
            Understand your dataset, columns, data types,
            missing values and duplicate records.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col2:

        st.markdown(
            """
            <div class="feature-box">

            <h3>📈 Visualize</h3>

            <p>
            Create histograms, bar charts and scatter plots
            to understand patterns in your data.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    with col3:

        st.markdown(
            """
            <div class="feature-box">

            <h3>🧠 Ask AI</h3>

            <p>
            Ask questions about your dataset and receive
            data-driven explanations.
            </p>

            </div>
            """,
            unsafe_allow_html=True
        )

    st.markdown("## 💬 Example Questions")

    questions = [
        "💡 Which region has the highest sales?",
        "💡 Which category generates the most profit?",
        "💡 What is the average sales?",
        "💡 Which customer segment has the highest sales?",
        "💡 What is the relationship between discount and profit?"
    ]

    for question in questions:
        st.write(question)

    st.markdown("---")

    st.markdown(
        """
        <div style="text-align:center;">

        <strong>
        Built with Python • Pandas • Streamlit • OpenAI
        </strong>

        <br>

        Developed by Pratik Choudhary

        </div>
        """,
        unsafe_allow_html=True
    )

    # Stop the application here.
    # Therefore AI analysis cannot appear on Home page.
    st.stop()


# =========================================================
# LOAD DATA
# =========================================================

try:

    upload_folder = "data/uploads"

    os.makedirs(
        upload_folder,
        exist_ok=True
    )

    file_path = os.path.join(
        upload_folder,
        uploaded_file.name
    )

    with open(file_path, "wb") as file:

        file.write(
            uploaded_file.getbuffer()
        )

    df = load_data(file_path)

    validate_data(df)

    profile = profile_data(df)

except Exception as e:

    st.error(
        f"❌ Error loading dataset: {e}"
    )

    st.stop()


# =========================================================
# DATASET SUCCESS MESSAGE
# =========================================================

st.success(
    f"✅ Dataset loaded successfully: "
    f"{len(df):,} rows × {len(df.columns)} columns"
)


# =========================================================
# TABS
# =========================================================

tab1, tab2, tab3, tab4 = st.tabs(
    [
        "📊 Data Explorer",
        "📈 Visualizations",
        "🧠 AI Analyst",
        "🔍 Data Quality"
    ]
)


# =========================================================
# TAB 1 — DATA EXPLORER
# =========================================================

with tab1:

    st.subheader("📊 Dataset Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        st.metric(
            "Rows",
            f"{len(df):,}"
        )

    with col2:

        st.metric(
            "Columns",
            len(df.columns)
        )

    with col3:

        st.metric(
            "Duplicate Rows",
            int(df.duplicated().sum())
        )

    with col4:

        st.metric(
            "Missing Values",
            int(df.isna().sum().sum())
        )

    st.markdown("### 👀 Preview")

    st.dataframe(
        df.head(20),
        use_container_width=True
    )

    st.markdown("### 🧾 Column Information")

    column_information = pd.DataFrame(
        {
            "Column": df.columns,

            "Data Type": [
                str(df[column].dtype)
                for column in df.columns
            ],

            "Missing": [
                int(df[column].isna().sum())
                for column in df.columns
            ],

            "Unique Values": [
                int(df[column].nunique())
                for column in df.columns
            ]
        }
    )

    st.dataframe(
        column_information,
        use_container_width=True
    )


# =========================================================
# TAB 2 — VISUALIZATIONS
# =========================================================

with tab2:

    st.subheader("📈 Data Visualization")

    st.write(
        "Explore patterns, distributions and relationships "
        "in your dataset."
    )

    st.markdown("---")

    # =====================================================
    # VISUALIZATION CONTROLS
    # =====================================================

    col1, col2 = st.columns([1, 2])

    with col1:

        chart_type = st.selectbox(
            "📊 Choose Chart",
            [
                "Histogram",
                "Bar Chart",
                "Scatter Plot"
            ]
        )

    with col2:

        if chart_type == "Histogram":

            st.info(
                "Shows how values are distributed."
            )

        elif chart_type == "Bar Chart":

            st.info(
                "Compares values across categories."
            )

        else:

            st.info(
                "Shows the relationship between "
                "two numeric variables."
            )

    st.markdown("---")


    # =====================================================
    # HISTOGRAM
    # =====================================================

    if chart_type == "Histogram":

        if len(profile["numeric_columns"]) == 0:

            st.warning(
                "⚠️ No numeric columns available."
            )

        else:

            numeric_columns = profile[
                "numeric_columns"
            ]

            selected_column = st.selectbox(
                "🔢 Select numeric column",
                numeric_columns,
                key="hist_column"
            )

            series = df[
                selected_column
            ].dropna()

            # KPI CARDS

            col1, col2, col3, col4 = st.columns(4)

            with col1:

                st.metric(
                    "Count",
                    f"{len(series):,}"
                )

            with col2:

                st.metric(
                    "Average",
                    f"{series.mean():,.2f}"
                )

            with col3:

                st.metric(
                    "Minimum",
                    f"{series.min():,.2f}"
                )

            with col4:

                st.metric(
                    "Maximum",
                    f"{series.max():,.2f}"
                )

            st.markdown(
                f"### 📊 Distribution of {selected_column}"
            )

            try:

                fig = histogram(
                    df,
                    selected_column
                )

                st.pyplot(
                    fig,
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"Unable to create histogram: {e}"
                )

            with st.expander(
                "🔍 View distribution statistics"
            ):

                st.dataframe(
                    df[
                        [selected_column]
                    ].describe(),
                    use_container_width=True
                )


    # =====================================================
    # BAR CHART
    # =====================================================

    elif chart_type == "Bar Chart":

        categorical_columns = profile[
            "categorical_columns"
        ]

        numeric_columns = profile[
            "numeric_columns"
        ]

        if (
            len(categorical_columns) == 0
            or len(numeric_columns) == 0
        ):

            st.warning(
                "⚠️ Bar chart requires both "
                "categorical and numeric columns."
            )

        else:

            col1, col2 = st.columns(2)

            with col1:

                category_column = st.selectbox(
                    "🏷️ Category",
                    categorical_columns,
                    key="bar_category"
                )

            with col2:

                value_column = st.selectbox(
                    "🔢 Numeric Value",
                    numeric_columns,
                    key="bar_value"
                )

            # GROUP DATA

            grouped_data = (
                df.groupby(
                    category_column
                )[value_column]
                .sum()
                .sort_values(
                    ascending=False
                )
                .head(10)
            )

            # KPI CARDS

            if len(grouped_data) > 0:

                top_category = grouped_data.index[0]

                top_value = grouped_data.iloc[0]

                col1, col2, col3 = st.columns(3)

                with col1:

                    st.metric(
                        "🏆 Top Category",
                        str(top_category)
                    )

                with col2:

                    st.metric(
                        "Highest Value",
                        f"{top_value:,.2f}"
                    )

                with col3:

                    st.metric(
                        "Categories Shown",
                        len(grouped_data)
                    )

            st.markdown(
                f"### 📊 {value_column} by "
                f"{category_column}"
            )

            try:

                fig = bar_chart(
                    df,
                    category_column,
                    value_column
                )

                st.pyplot(
                    fig,
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"Unable to create bar chart: {e}"
                )

            with st.expander(
                "🔍 View chart data"
            ):

                chart_data = (
                    grouped_data
                    .reset_index()
                )

                chart_data.columns = [
                    category_column,
                    value_column
                ]

                st.dataframe(
                    chart_data,
                    use_container_width=True
                )


    # =====================================================
    # SCATTER PLOT
    # =====================================================

    elif chart_type == "Scatter Plot":

        numeric_columns = profile[
            "numeric_columns"
        ]

        if len(numeric_columns) < 2:

            st.warning(
                "⚠️ Scatter plot requires at least "
                "two numeric columns."
            )

        else:

            col1, col2 = st.columns(2)

            with col1:

                column1 = st.selectbox(
                    "🔵 X-axis",
                    numeric_columns,
                    key="scatter_x"
                )

            with col2:

                column2 = st.selectbox(
                    "🟢 Y-axis",
                    numeric_columns,
                    key="scatter_y"
                )

            # CORRELATION

            correlation = df[
                column1
            ].corr(
                df[column2]
            )

            # RELATIONSHIP

            if correlation >= 0.7:

                relationship = (
                    "Strong positive relationship"
                )

            elif correlation >= 0.3:

                relationship = (
                    "Moderate positive relationship"
                )

            elif correlation > -0.3:

                relationship = (
                    "Weak or no linear relationship"
                )

            elif correlation > -0.7:

                relationship = (
                    "Moderate negative relationship"
                )

            else:

                relationship = (
                    "Strong negative relationship"
                )

            # VALID ROWS

            valid_rows = df[
                [column1, column2]
            ].dropna()

            # KPI CARDS

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Correlation",
                    f"{correlation:.3f}"
                )

            with col2:

                st.metric(
                    "Relationship",
                    relationship
                )

            with col3:

                st.metric(
                    "Data Points",
                    f"{len(valid_rows):,}"
                )

            # CHART

            st.markdown(
                f"### 📈 {column2} vs {column1}"
            )

            try:

                fig = scatter_plot(
                    df,
                    column1,
                    column2
                )

                st.pyplot(
                    fig,
                    use_container_width=True
                )

            except Exception as e:

                st.error(
                    f"Unable to create scatter plot: {e}"
                )

            # INTERPRETATION

            st.markdown(
                "### 🧠 Quick Interpretation"
            )

            st.info(
                f"The correlation between "
                f"**{column1}** and **{column2}** "
                f"is **{correlation:.3f}**. "
                f"This indicates a "
                f"**{relationship.lower()}**."
            )

            with st.expander(
                "🔍 View correlation data"
            ):

                st.dataframe(
                    valid_rows,
                    use_container_width=True
                )


# =========================================================
# TAB 3 — AI ANALYST
# =========================================================

with tab3:

    st.subheader(
        "🧠 Ask the AI Data Analyst"
    )

    st.write(
        "Ask a question about your uploaded dataset."
    )

    question = st.text_input(
        "💬 Your question",
        placeholder=(
            "Example: Which region has the highest sales?"
        )
    )

    analyze_clicked = st.button(
        "🔍 Analyze",
        type="primary"
    )

    # =====================================================
    # RUN AI ANALYSIS
    # =====================================================

    if analyze_clicked:

        if not question.strip():

            st.warning(
                "Please enter a question."
            )

        else:

            try:

                # STEP 1 — UNDERSTAND QUESTION

                with st.spinner(
                    "🧠 Understanding your question..."
                ):

                    analysis_plan = (
                        understand_question(
                            question,
                            profile
                        )
                    )

                analysis_type = (
                    analysis_plan.get(
                        "analysis_type"
                    )
                )

                column1 = (
                    analysis_plan.get(
                        "column1",
                        ""
                    )
                )

                column2 = (
                    analysis_plan.get(
                        "column2",
                        ""
                    )
                )

                # STEP 2 — PERFORM ANALYSIS

                with st.spinner(
                    "📊 Analyzing your data..."
                ):

                    analysis_result = None

                    if analysis_type == "statistics":

                        if column1 not in df.columns:

                            raise ValueError(
                                f"Column '{column1}' "
                                "does not exist."
                            )

                        analysis_result = (
                            calculate_statistics(
                                df,
                                column1
                            )
                        )

                    elif analysis_type == "group_analysis":

                        if (
                            column1 not in df.columns
                            or column2 not in df.columns
                        ):

                            raise ValueError(
                                "Invalid columns selected "
                                "for group analysis."
                            )

                        analysis_result = (
                            group_analysis(
                                df,
                                column1,
                                column2
                            )
                        )

                    elif analysis_type == "correlation":

                        if (
                            column1 not in df.columns
                            or column2 not in df.columns
                        ):

                            raise ValueError(
                                "Invalid columns selected "
                                "for correlation."
                            )

                        analysis_result = (
                            calculate_correlation(
                                df,
                                column1,
                                column2
                            )
                        )

                    elif analysis_type == "column_summary":

                        if column1 not in df.columns:

                            raise ValueError(
                                f"Column '{column1}' "
                                "does not exist."
                            )

                        analysis_result = (
                            column_summary(
                                df,
                                column1
                            )
                        )

                    elif analysis_type == "top_categories":

                        if column1 not in df.columns:

                            raise ValueError(
                                f"Column '{column1}' "
                                "does not exist."
                            )

                        analysis_result = (
                            top_categories(
                                df,
                                column1
                            )
                        )

                    else:

                        raise ValueError(
                            f"Unsupported analysis type: "
                            f"{analysis_type}"
                        )

                # RAW RESULT

                with st.expander(
                    "🔍 View raw analysis result"
                ):

                    if isinstance(
                        analysis_result,
                        pd.DataFrame
                    ):

                        st.dataframe(
                            analysis_result,
                            use_container_width=True
                        )

                    else:

                        st.json(
                            analysis_result
                        )

                # STEP 3 — GENERATE ANSWER

                with st.spinner(
                    "✍️ Generating explanation..."
                ):

                    answer = generate_answer(
                        question,
                        analysis_result
                    )

                # AI INSIGHTS

                st.markdown("---")

                st.subheader(
                    "💡 AI Insights"
                )

                if answer.get(
                    "key_finding"
                ):

                    st.markdown(
                        f"""
                        <div class="insight-box">

                        <div class="insight-title">
                        🎯 Key Finding
                        </div>

                        <div class="insight-text">
                        {answer["key_finding"]}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if answer.get(
                    "evidence"
                ):

                    st.markdown(
                        f"""
                        <div class="insight-box">

                        <div class="insight-title">
                        📊 Evidence
                        </div>

                        <div class="insight-text">
                        {answer["evidence"]}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if answer.get(
                    "interpretation"
                ):

                    st.markdown(
                        f"""
                        <div class="insight-box">

                        <div class="insight-title">
                        🧠 Interpretation
                        </div>

                        <div class="insight-text">
                        {answer["interpretation"]}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

                if answer.get(
                    "data_note"
                ):

                    st.markdown(
                        f"""
                        <div class="insight-box">

                        <div class="insight-title">
                        ⚠️ Data Note
                        </div>

                        <div class="insight-text">
                        {answer["data_note"]}
                        </div>

                        </div>
                        """,
                        unsafe_allow_html=True
                    )

            except Exception as e:

                st.error(
                    f"❌ Analysis failed: {e}"
                )


# =========================================================
# TAB 4 — DATA QUALITY
# =========================================================

with tab4:

    st.subheader(
        "🔍 Data Quality"
    )

    # MISSING VALUES

    st.markdown(
        "### Missing Values"
    )

    missing_data = pd.DataFrame(
        {
            "Column": df.columns,

            "Missing Values": [
                int(df[column].isna().sum())
                for column in df.columns
            ]
        }
    )

    missing_data = missing_data[
        missing_data["Missing Values"] > 0
    ]

    if missing_data.empty:

        st.success(
            "✅ No missing values found."
        )

    else:

        st.dataframe(
            missing_data,
            use_container_width=True
        )

    # DUPLICATES

    st.markdown(
        "### Duplicate Rows"
    )

    duplicate_count = int(
        df.duplicated().sum()
    )

    if duplicate_count == 0:

        st.success(
            "✅ No duplicate rows found."
        )

    else:

        st.warning(
            f"⚠️ {duplicate_count:,} duplicate "
            "rows found."
        )

    # DATA TYPES

    st.markdown(
        "### Data Types"
    )

    dtype_data = pd.DataFrame(
        {
            "Column": df.columns,

            "Data Type": [
                str(df[column].dtype)
                for column in df.columns
            ]
        }
    )

    st.dataframe(
        dtype_data,
        use_container_width=True
    )


# =========================================================
# FOOTER
# =========================================================

st.markdown("---")

st.markdown(
    """
    <div style="text-align:center;">

    <strong>
    Built with Python • Pandas • Streamlit • OpenAI
    </strong>

    <br>

    Developed by Pratik Choudhary

    </div>
    """,
    unsafe_allow_html=True
)