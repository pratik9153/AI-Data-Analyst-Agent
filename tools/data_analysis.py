import pandas as pd


def column_summary(
    df: pd.DataFrame,
    column: str
):

    return {
        "column": column,

        "data_type": str(
            df[column].dtype
        ),

        "missing_values": int(
            df[column].isna().sum()
        ),

        "unique_values": int(
            df[column].nunique()
        )
    }


def group_analysis(
    df: pd.DataFrame,
    category_column: str,
    value_column: str
):

    result = (
        df.groupby(
            category_column
        )[value_column]
        .agg(
            ["sum", "mean", "count"]
        )
        .sort_values(
            "sum",
            ascending=False
        )
        .head(10)
    )

    return result.reset_index()


def top_categories(
    df: pd.DataFrame,
    column: str
):

    result = (
        df[column]
        .value_counts()
        .head(10)
        .reset_index()
    )

    result.columns = [
        column,
        "count"
    ]

    return result