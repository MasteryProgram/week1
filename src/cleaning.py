import pandas as pd


def remove_nulls(df):
    """
    Remove missing values.
    """
    return df.dropna()


def remove_duplicates(df):
    """
    Remove duplicate rows.
    """
    return df.drop_duplicates()


def convert_datetime(df, column):
    """
    Convert column to datetime.
    """
    df[column] = pd.to_datetime(df[column])
    return df




def normalize_timezone(df, column='date', timezone='UTC'):
    """
    Convert datetime column to a consistent timezone.
    """

    df[column] = pd.to_datetime(
        df[column],
        format='mixed',
        utc=True
    )

    df[column] = df[column].dt.tz_convert(timezone)

    return df