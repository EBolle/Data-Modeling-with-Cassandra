"""Helper functions to create or validate data."""


import pandas as pd
import pathlib


def create_csv_path_list(file_path: pathlib.Path) -> list:
    """
    Returns a list of Paths of all files which ends with .csv in the file_path, including all subdirectories.

    Example
        from pathlib import Path

        data_path = Path('.') / 'data'
        csv_path_list = create_csv_path_list(data_path)
    """
    try:
        return_list = [x for x in file_path.glob("**/*.csv")]
    except AttributeError as err:
        print(f"The input is invalid, make sure it is a Path like object, error: {err}")
    else:
        print(f"{file_path} contains {len(return_list)} .csv files.")
        if return_list:
            return return_list


def unique_key_check(df: pd.DataFrame, keys: list) -> bool:
    """
    Returns TRUE when the combination of keys is unique, these keys can then be used as primary index.
    """
    if not df.shape[0]:
        raise ValueError(f"df has {df.shape[0]} rows, please check your input.")

    if not isinstance(keys, list):
        raise ValueError("The keys parameter must be a list.")

    df.columns = df.columns.str.lower()
    lower_keys = [key.lower() for key in keys]

    if not all([item in df.columns for item in lower_keys]):
        raise ValueError("Not all keys are present in the columns of df, please check your input.")

    keys_rows = df.groupby(lower_keys).size().reset_index().shape[0]
    df_rows = df.shape[0]

    return keys_rows == df_rows
