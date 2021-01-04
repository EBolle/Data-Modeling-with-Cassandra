"""Helper functions for various steps in the overall process."""

import pandas as pd


def create_csv_path_list(file_path: str) -> list:
    """
    Returns a list of .csv Paths in the file_path, including all subdirectories.

    Example
        from pathlib import Path

        data_path = Path('.') / 'data'
        csv_path_list = create_csv_path_list(data_path)
    """
    return_list = [x for x in file_path.glob("**/*.csv")]
    print(f"{file_path} contains {len(return_list)} .csv files.")

    return return_list


def unique_key_check(df: pd.DataFrame, keys: list) -> pd.DataFrame:
    """
    Returns TRUE when the combination of keys is unique, these keys can then be used as primary index.
    """
    if not all([item in df.columns for item in keys]):
        raise ValueError("The keys are not present in the columns of df, please check again.")

    keys_rows = df.groupby(keys).size().reset_index().shape[0]
    df_rows = df.shape[0]

    return keys_rows == df_rows
