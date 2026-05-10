import pandas as pd


def load_data(filepath, index_col=None, parse_dates=False):
    """
    Load CSV dataset into pandas DataFrame.
    """

    df = pd.read_csv(
        filepath,
        index_col=index_col,
        parse_dates=parse_dates
    )

    return df