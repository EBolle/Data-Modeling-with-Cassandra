## Speed is of the essence 

<img src="https://images.pexels.com/photos/290470/pexels-photo-290470.jpeg?auto=compress&cs=tinysrgb&dpr=1&w=800">

Source: https://www.pexels.com

After carefully analyzing the behaviour of our users, the analytics team proposed a few very successful user stories
which significantly contributed to the growth of Sparkify. To avoid being perished by their own success, the analytics
team needed a serious performance upgrade when it comes to querying the database. Since speed is the most important
factor for the analytics teams, we have decided to create a Cassandra database, specifically optimized for certain
queries.

### The queries and primary keys

Based on the requests of the queries we have decided to create 3 tables:
- session_info: returns the artist, song and the length of the song based on session id and item in session
- user_info: returns the artist, song, and the first and last name of the user based on the user id and session id, for
analytical purposes the items in the session are sorted
- user_info_per_song: returns the first and last name of the users based on the song

To give you a head start, hereby are some example queries you easily modify and use for your own purposes.

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

### Instructions

This project revolves around a single jupyter notebook, stored in notebooks/main.ipynb. This notebook includes every
step in the process, additional explanation and comments when necessary, and visual support for choosing the partition
keys. Before you can run the notebook, there are a few things you need to do:
- create and activate a virtual environment
- run the tests

Furthermore, note that the logic needed to execute the notebook is stored in the /src folder. The Python version used
for this project is 3.8.5. 

#### create and activate a virtual environment 

You can either use Anaconda or venv to create the virtual environment. Regardless of your choice, you have to open
a (Anaconda) prompt, clone the project, and navigate to the project folder. Next, enter the following:

##### Anaconda
```bash
conda env create -f environment.yml
conda activate postgres
```

##### venv
```bash
python -m venv venv
venv\Scripts\Activate
pip install -r requirements.txt 
```

#### Tests

```bash
pytest -v
```

### Contact

In case of suggestions or remarks please contact the Data Engineering department.