# Speed is of the essence 

After carefully analyzing the behaviour of our users, the analytics team proposed a few very successful user stories
which significantly contributed to the growth of Sparkify. To avoid being perished by their own success, the analytics
team needed a serious performance upgrade when it comes to querying the database. Since speed is the most important
factor for the analytics teams, we have decided to create a Cassandra database, specifically optimized for certain
queries.

## Example queries

Based on the requests of the queries we have decided to create 3 tables:
- session_info: returns the artist, song and the length of the song based on session id and item in session
- user_info: returns the artist, song, and the first and last name of the user based on the user id and session id, for
analytical purposes the items in the session are sorted
- user_info_per_song: returns the first and last name of the users based on the song

To give you a head start, hereby are some example queries you can easily modify and use for your own purposes.

```sql
SELECT artist
,    song
,    song_length

FROM
    session_info
    
WHERE
    session_id=338
and item_in_session=4
```

```sql
SELECT artist
,    song
,    first_name
,    last_name

FROM
    user_info
    
WHERE
    user_id=10
and session_id=182
```

```sql
SELECT first_name
,    last_name

FROM
    user_info_per_song
    
WHERE
    song='All Hands Against His Own'
```

## Instructions

This project revolves around a single jupyter notebook, stored in notebooks/main.ipynb. This notebook includes every
step in the process, additional explanation and comments when necessary, and visual support for choosing the partition
keys. Before you can run the notebook, there are a few things you need to do:

- create and activate a virtual environment
- run the tests

Furthermore, note that the logic needed to execute the notebook is stored in the /src folder. The Python version used
for this project is 3.8.5. 

### create and activate a virtual environment 

You can either use Anaconda or virtualenv to create the virtual environment, if you are not familiar with virtual
environments please read this [article][virtual_envs] first.

```bash
conda env create -f environment.yml
conda activate cassandra

python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt 
```

### Tests

To make the code more robust, several tests were added to guarantee the code works and keeps working as intended. Before
you start exploring the notebook it is recommended to run the tests first.

```bash
pytest -v
```

## Contact

In case of suggestions or remarks please contact the Data Engineering department.

[virtual_envs]: https://realpython.com/python-virtual-environments-a-primer/