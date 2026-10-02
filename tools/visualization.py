from visualization.charts import (
    create_histogram,
    create_bar_chart,
    create_scatter_plot
)


def histogram(
    df,
    column
):

    return create_histogram(
        df,
        column
    )


def bar_chart(
    df,
    category_column,
    value_column
):

    return create_bar_chart(
        df,
        category_column,
        value_column
    )


def scatter_plot(
    df,
    column1,
    column2
):

    return create_scatter_plot(
        df,
        column1,
        column2
    )