"""Tests the create_csv_path_list and unique_key_check functions from src/data_utils.py"""


import pandas as pd
import pathlib
from pathlib import Path
import pytest
from src.data_utils import create_csv_path_list, unique_key_check


class TestCreateCsvPathList:
    """
    Tests the behaviour of the create_csv_path_list function with different input values.
    """
    def test_correct_input(self, temp_csv_dir):
        """
        Tests several characteristics of a valid and non-empty csv_path_list.
        """
        temp_path = Path(temp_csv_dir)
        csv_path_list = create_csv_path_list(temp_path)

        assert len(csv_path_list) == 1
        assert csv_path_list[0].name == 'example.csv'
        assert isinstance(csv_path_list[0], (pathlib.WindowsPath, pathlib.PosixPath))

    @pytest.mark.parametrize('wrong_input', [0, 1.25, 'test', [], (), {}])
    def test_wrong_input(self, wrong_input):
        """
        Passing anything but a Path like object should return a print statement, and therefore equal None.
        """
        assert create_csv_path_list(wrong_input) is None


class TestUniqueKeyCheck:
    """
    Tests the behaviour of unique_key_check with different input values, and makes sure the correct exceptions
    and informative messages are raised.
    """
    @pytest.mark.parametrize('wrong_input_keys', [0, 1.25, 'test', (), {}, ('test_1', 'test_2'), {'test': 'test'}])
    def test_wrong_input_keys(self, wrong_input_keys):
        """
        Passing anything but a list as the 'keys' parameter should raise a ValueError, and return an
        informative exception message.
        """
        valid_test_df = pd.DataFrame({'test_values': [0, 1, 2, 3]})
        with pytest.raises(ValueError) as exc_info:
            unique_key_check(valid_test_df, wrong_input_keys)

        exception_msg = exc_info.value.args[0]
        assert exception_msg == 'The keys parameter must be a list.'

    def test_raises_empty_df(self):
        """
        A ValueError should be raised when passed an empty Pandas DataFrame, and return an
        informative exception message.
        """
        empty_df = pd.DataFrame()
        with pytest.raises(ValueError) as exc_info:
            unique_key_check(empty_df, ['a_none_empty_list'])

        exception_msg = exc_info.value.args[0]
        assert exception_msg == 'df has 0 rows, please check your input.'

    def test_raises_keys_not_present(self):
        """
        A ValueError should be raised when passed keys which are not present in the df, and return an informative
        exception message.
        """
        valid_test_df = pd.DataFrame({'valid_column_name': [0, 1, 2, 3]})
        non_valid_key = ['not_present_in_valid_test_df']
        with pytest.raises(ValueError) as exc_info:
            unique_key_check(valid_test_df, non_valid_key)

        exception_msg = exc_info.value.args[0]
        assert exception_msg == 'Not all keys are present in the columns of df, please check your input.'

    def test_correct_input_1(self):
        """
        Given a unique key the function should return TRUE, even with different upper/lower column cases.
        """
        valid_test_df = pd.DataFrame({'valid_column_name': [0, 1, 2, 3]})
        valid_key = ['VALID_column_NAME']

        assert unique_key_check(valid_test_df, valid_key) is True

    def test_correct_input_2(self):
        """
        Given the dataframe and the keys, a single key should return FALSE while both keys should return TRUE.
        """
        valid_test_df = pd.DataFrame({'first_column': [0, 0, 1, 2],
                                      'second_column': [1, 2, 3, 3]})

        assert unique_key_check(valid_test_df, ['first_column']) is False
        assert unique_key_check(valid_test_df, ['second_column']) is False
        assert unique_key_check(valid_test_df, ['first_column', 'second_column']) is True
