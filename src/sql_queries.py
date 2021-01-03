"""DROP, CREATE, and INSERT queries for the 3 specific insights we want to gather from the data."""


# DROP

session_info_drop = "DROP TABLE IF EXISTS session_info"
user_info_drop = "DROP TABLE IF EXISTS user_info"
user_info_per_song_drop = "DROP TABLE IF EXISTS user_info_per_song"

# CREATE

session_info_create = """ 
CREATE TABLE IF NOT EXISTS session_info (
artist text,
song text,
song_length float,
session_id int,
item_in_session int,
PRIMARY KEY (session_id, item_in_session)
)
"""

user_info_create = """ 
CREATE TABLE IF NOT EXISTS user_info (
artist text,
song text,
first_name text,
last_name text,
session_id int,
user_id int,
item_in_session int,
PRIMARY KEY (session_id, user_id, item_in_session)
)
"""

user_info_per_song_create = """ 
CREATE TABLE IF NOT EXISTS user_info_per_song (
first_name text,
last_name text,
song text,
session_id int,
item_in_session int,
PRIMARY KEY (song, session_id, session_id, item_in_session)
)
"""

# INSERT

session_info_insert = """
INSERT INTO song_length (artist, song, song_length, session_id, item_in_session)
VALUES (%s, %s, %s, %s, %s)
"""

user_info_insert = """
INSERT INTO user_info (artist, song, first_name, last_name, session_id, user_id, item_in_session)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

user_info_per_song_insert = """
INSERT INTO user_info_per_song (first_name, last_name, song, session_id, item_in_session)
VALUES (%s, %s, %s, %s, %s)
"""

# QUERY LISTS

drop_list = [session_info_drop, user_info_drop, user_info_per_song_drop]
create_list = [session_info_create, user_info_create, user_info_per_song_create]
insert_list = [session_info_insert, user_info_insert, user_info_per_song_insert]