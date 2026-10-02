import matplotlib.pyplot as plt


def create_histogram(
    df,
    column
):

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.hist(
        df[column].dropna(),
        bins=20
    )

    ax.set_title(
        f"Distribution of {column}"
    )

    ax.set_xlabel(column)
    ax.set_ylabel("Frequency")

    fig.tight_layout()

    return fig


def create_bar_chart(
    df,
    category_column,
    value_column
):

    grouped = (
        df.groupby(
            category_column
        )[value_column]
        .sum()
        .sort_values(
            ascending=False
        )
        .head(10)
    )

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    grouped.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(
        f"{value_column} by {category_column}"
    )

    ax.set_xlabel(
        category_column
    )

    ax.set_ylabel(
        value_column
    )

    plt.xticks(
        rotation=45
    )

    fig.tight_layout()

    return fig


def create_scatter_plot(
    df,
    column1,
    column2
):

    fig, ax = plt.subplots(
        figsize=(8, 4)
    )

    ax.scatter(
        df[column1],
        df[column2]
    )

    ax.set_title(
        f"{column2} vs {column1}"
    )

    ax.set_xlabel(column1)
    ax.set_ylabel(column2)

    fig.tight_layout()

    return fig