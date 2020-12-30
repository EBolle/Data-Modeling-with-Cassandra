"""Helper function to collect a list of .csv files."""


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
