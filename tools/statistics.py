import pandas as pd


def calculate_statistics(
    df: pd.DataFrame,
    column: str
):

    series = df[column].dropna()

    return {
        "column": column,
        "count": int(series.count()),
        "mean": round(
            float(series.mean()),
            2
        ),
        "median": round(
            float(series.median()),
            2
        ),
        "minimum": round(
            float(series.min()),
            2
        ),
        "maximum": round(
            float(series.max()),
            2
        )
    }


def calculate_correlation(
    df: pd.DataFrame,
    column1: str,
    column2: str
):

    correlation = df[
        column1
    ].corr(
        df[column2]
    )

    return {
        "column1": column1,
        "column2": column2,
        "correlation": round(
            float(correlation),
            3
        )
    }