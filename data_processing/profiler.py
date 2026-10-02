def profile_data(df):

    numeric_columns = list(
        df.select_dtypes(
            include="number"
        ).columns
    )

    categorical_columns = list(
        df.select_dtypes(
            include=["object", "category"]
        ).columns
    )

    datetime_columns = list(
        df.select_dtypes(
            include=["datetime"]
        ).columns
    )

    profile = {

        "rows": len(df),

        "columns": len(df.columns),

        "column_names": list(
            df.columns
        ),

        "data_types": {
            column: str(
                df[column].dtype
            )
            for column in df.columns
        },

        "missing_values": {
            column: int(
                df[column].isna().sum()
            )
            for column in df.columns
        },

        "duplicate_rows": int(
            df.duplicated().sum()
        ),

        "numeric_columns": numeric_columns,

        "categorical_columns": categorical_columns,

        "datetime_columns": datetime_columns
    }

    return profile