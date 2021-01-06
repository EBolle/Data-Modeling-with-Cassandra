"""This module makes sure the temp_csv_dir fixture can be used by both test_ modules."""


import csv
import pytest


@pytest.fixture()
def temp_csv_dir(tmpdir):
    """
    Temporary directory with a single .csv file which includes 1 row of the actual files used in the project.
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
