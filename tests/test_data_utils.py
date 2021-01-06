# fixture Path list -> returns something? What happens when we insert something else?


from pathlib import Path
import pytest
from src.data_utils import create_csv_path_list, unique_key_check


@pytest.fixture()
def temp_csv_dir(tmpdir):
    """
    Temporary directory with .csv files that can be used by several of the tests within this module (fixture).
    """
    event_data = tmpdir.mkdir('event_data')
    example_csv = event_data.join('example.csv')
    example_csv.write("""
    artist,auth,firstName,gender,itemInSession,lastName,length,level,location,method,page,
    registration,sessionId,song,status,ts,userId
    """)
    example_csv.write("""
    Infected Mushroom,Logged In,Kaylee,F,6,Summers,440.2673,free,"Phoenix-Mesa-Scottsdale,
    AZ", PUT,NextSong, 1.54034E+12,139,Becoming Insane,200,1.54111E+12,8
    """)

    return event_data


def test_temp_dir(temp_csv_dir):
    temp_path = Path(temp_csv_dir)
    csv_path_list = create_csv_path_list(temp_path)
    print(csv_path_list)

    assert len(csv_path_list) == 1


@pytest.mark.parametrize('wrong_input', [0, 1.25, 'test', [], (), {}])
def test_csv_list_wrong_input(wrong_input):
    """
    Passing anything but a Path like object should return a print statement, and therefore equal None.
    """
    assert create_csv_path_list(wrong_input) is None


def test_csv_list_correct_but_empty_input():
    """
    Passing a correct but empty Path like object should only return a print statement, and therefore equal a NoneType.
    """
    empty_path = Path('.') / 'tests'
    empty_path_csv_list = create_csv_path_list(empty_path)

    assert empty_path_csv_list is None


def test_csv_list_correct_input():
    """
    Passing a correct Path like object with .csv files should return a list of Path like objects.
    CREATE a temporary directory with fake .csv files -> fixtures -> read?
    """
    correct_path = Path('.') / 'event_data'
    correct_path_csv_list = create_csv_path_list(correct_path)

    assert type(correct_path_csv_list) == list
    assert len(correct_path_csv_list) > 0
