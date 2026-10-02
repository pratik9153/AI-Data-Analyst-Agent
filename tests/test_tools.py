import pandas as pd

from tools.statistics import (
    calculate_statistics
)


def test_statistics():

    df = pd.DataFrame(
        {
            "sales": [
                10,
                20,
                30
            ]
        }
    )

    result = calculate_statistics(
        df,
        "sales"
    )

    assert result["mean"] == 20

    assert result["minimum"] == 10

    assert result["maximum"] == 30