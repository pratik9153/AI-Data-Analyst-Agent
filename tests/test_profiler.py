import pandas as pd

from data_processing.profiler import profile_data


def test_profile_data():

    df = pd.DataFrame(
        {
            "name": [
                "A",
                "B",
                "C"
            ],

            "age": [
                20,
                21,
                22
            ]
        }
    )

    result = profile_data(df)

    assert result["rows"] == 3

    assert result["columns"] == 2

    assert "age" in result[
        "numeric_columns"
    ]