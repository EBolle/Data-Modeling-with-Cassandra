

import csv
import pandas as pd
import pathlib
from pathlib import Path
import pytest
from src.data_utils import create_csv_path_list, unique_key_check


@pytest.fixture()
def temp_csv_dir(tmpdir):
    """
    Temporary directory with a single .csv file which includes 1 rows of the actual files used in the project.
    This directory can be used by several of the tests throughout the project.
    """
    event_data = tmpdir.mkdir('event_data')
    example_csv = event_data.join('example.csv')

    with open(example_csv, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['artist', 'auth', 'firstName', 'gender', 'itemInSession', 'lastName', 'length', 'level',
                         'location', 'method', 'page', 'registration', 'sessionId', 'song', 'status', 'ts', 'userId'])
        writer.writerow(['Infected Mushroom', 'Logged In', 'Kaylee', 'F', '6', 'Summers', '440.2673', 'free',
                         "Phoenix-Mesa-Scottsdale, AZ", 'PUT', 'NextSong', '1.54034E+12,139', '139', 'Becoming Insane',
                         '200', '1.54111E+12', '8'])

    return event_data


def test_csv_list_correct_input(temp_csv_dir):
    """
    Tests several characteristics of a valid and non-empty csv_path_list.
    """
    temp_path = Path(temp_csv_dir)
    csv_path_list = create_csv_path_list(temp_path)

    assert len(csv_path_list) == 1
    assert csv_path_list[0].name == 'example.csv'
    assert isinstance(csv_path_list[0], (pathlib.WindowsPath, pathlib.PosixPath))


@pytest.mark.parametrize('wrong_input', [0, 1.25, 'test', [], (), {}])
def test_csv_list_wrong_input(wrong_input):
    """
    Passing anything but a Path like object should return a print statement, and therefore equal None.
    """
    assert create_csv_path_list(wrong_input) is None


@pytest.mark.parametrize('wrong_input_keys', [0, 1.25, 'test', (), {}, ('test_1', 'test_2'), {'test': 'test'}])
def test_unique_key_check_raises(wrong_input_keys):
    valid_test_df = pd.DataFrame({'test_values': [0, 1, 2, 3]})
    with pytest.raises(ValueError):
        unique_key_check(valid_test_df, wrong_input_keys)
