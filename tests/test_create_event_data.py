"""
This module revolves around 1 test of the data_pipeline method of the CreateEventData class in src/create_event_data.py.
This test is very important since a lot of moving parts are involved to go from the raw .csv to a cleaned and
transformed Pandas dataframe.
"""


import pandas as pd
from pathlib import Path
from src.create_event_data import CreateEventData
from src.data_utils import create_csv_path_list


def test_data_pipeline(temp_csv_dir):
    """
    Tests whether the data_pipeline method converts the raw .csv fixture to the correct dataframe.
    """
    # Actual dataframe
    temp_path = Path(temp_csv_dir)
    csv_path_list = create_csv_path_list(temp_path)

    create_event_instance = CreateEventData(csv_path_list=csv_path_list)
    actual_df = create_event_instance.data_pipeline()

    # Expected dataframe
    columns = ['artist', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', 'level', 'location',
               'sessionId', 'song', 'userId']
    data_types = {'artist': str,
                  'firstName': str,
                  'gender': str,
                  'itemInSession': int,
                  'lastName': str,
                  'length': float,
                  'level': str,
                  'location': str,
                  'sessionId': int,
                  'song': str,
                  'userId': int}
    values = ['Infected Mushroom', 'Kaylee', 'F', '6', 'Summers', '440.2673', 'free', "Phoenix-Mesa-Scottsdale, AZ",
              '139', 'Becoming Insane', '8']

    expected_df = pd.DataFrame({key: value for key, value in zip(columns, values)}, index=range(1))
    expected_df = expected_df.astype(data_types)

    assert actual_df.equals(expected_df) is True
