import pandas as pd

from utils.exceptions import InvalidDataError


def validate_data(df):

    if not isinstance(df, pd.DataFrame):
        raise InvalidDataError(
            "Input is not a Pandas DataFrame."
        )

    if df.empty:
        raise InvalidDataError(
            "Dataset is empty."
        )

    if len(df.columns) == 0:
        raise InvalidDataError(
            "Dataset has no columns."
        )

    return True