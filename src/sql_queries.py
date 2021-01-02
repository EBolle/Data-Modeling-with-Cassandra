"""DROP, CREATE, and INSERT queries for the 3 specific insights we want to gather from the data."""


# DROP

song_length_table_drop = "DROP TABLE IF EXISTS song_length"
user_table_drop = "DROP TABLE IF EXISTS "
songs_table_drop = "DROP TABLE IF EXISTS sogs"


# CREATE

song_length_create = """ 
CREATE TABLE IF NOT EXISTS song_length (
artist text,
song text,
song_length float,
session_id int,
item_in_session int,
PRIMARY KEY (session_id, item_in_session)
)
"""

# INSERT

song_length_insert = """
INSERT INTO song_length (artist, song, song_length, session_id, item_in_session)
VALUES (%s, %s, %s, %s, %s)
"""






# QUERY LISTS

drop_list = [song_length_table_drop]
create_list = [song_length_create]
insert_list = [song_length_insert]