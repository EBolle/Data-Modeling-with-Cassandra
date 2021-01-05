# fixture Path list -> returns something? What happens when we insert something else?


from pathlib import Path
from src.data_utils import create_csv_path_list, unique_key_check


def test_csv_list_wrong_input():
    """
    Passing an integer, string, or empty list should return a print statement, and therefore equal a NoneType.
    """
    integer_csv_list = create_csv_path_list(0)
    string_csv_list = create_csv_path_list('test')
    list_csv_list = create_csv_path_list([])

    assert integer_csv_list == None
    assert string_csv_list == None
    assert list_csv_list == None


def test_csv_list_correct_but_empty_input():
    """
    Passing a correct but empty Path like object should only return a print statement, and therefore equal a NoneType.
    """
    empty_path = Path('.') / 'tests'
    empty_path_csv_list = create_csv_path_list(empty_path)

    assert empty_path_csv_list == None


def test_csv_list_correct_input():
    """
    Passing a correct Path like object with .csv files should return a list of Path like objects.
    CREATE a temporary directory with fake .csv files -> fixtures -> read?
    """
    correct_path = Path('.') / 'event_data'
    correct_path_csv_list = create_csv_path_list(correct_path)

    assert type(correct_path_csv_list) == list
    assert len(correct_path_csv_list) > 0
