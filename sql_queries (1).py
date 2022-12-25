# DROP TABLES if they dont't exist to create new ones.

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs "
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATING NEW TABLES

songplay_table_create = (""" 
CREATE TABLE IF NOT EXISTS songplays (\
    songplay_id SERIAL PRIMARY KEY, \
    start_time TIMESTAMP NOT NULL, \
    user_id VARCHAR NOT NULL, \
    level CHAR(30) NOT NULL, \
    song_id VARCHAR, \
    artist_id VARCHAR, \
    session_id INT NOT NULL, \
    location VARCHAR NOT NULL, \
    user_agent VARCHAR NOT NULL
    );
""")

user_table_create = (""" 
CREATE TABLE IF NOT EXISTS users (\
    user_id VARCHAR PRIMARY KEY NOT NULL, \
    first_name VARCHAR NOT NULL, \
    last_name VARCHAR NOT NULL, \
    gender VARCHAR NOT NULL, \
    level VARCHAR(30) NOT NULL
    );
""")

song_table_create = (""" 
CREATE TABLE IF NOT EXISTS songs(\
    song_id VARCHAR PRIMARY KEY, \
    title VARCHAR NOT NULL, \
    artist_id VARCHAR, \
    year INT NOT NULL, \
    duration FLOAT NOT NULL
    );
""")

artist_table_create = (""" 
CREATE TABLE IF NOT EXISTS artists(\
    artist_id VARCHAR PRIMARY KEY,\
    artist_name VARCHAR NOT NULL, \
    artist_location VARCHAR NOT NULL, \
    artist_latitude  float NOT NULL, \
    artist_longitude float NOT NULL
    );
""")

time_table_create = (""" 
CREATE TABLE IF NOT EXISTS time (\
    start_time TIMESTAMP PRIMARY KEY NOT NULL, \
    hour INT NOT NULL, \
    day INT NOT NULL, \
    week INT NOT NULL, \
    month INT NOT NULL, \
    year INT NOT NULL, \
    weekday INT NOT NULL
    );\
""")

# INSERT records for the tables we created above.

songplay_table_insert = (""" 
INSERT INTO songplays(
    start_time, 
    user_id, 
    level, 
    song_id, 
    artist_id, 
    session_id, 
    location, 
    user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s) ON CONFLICT (songplay_id) DO NOTHING
""")

user_table_insert = (""" 
INSERT INTO users(
    user_id, 
    first_name, 
    last_name, 
    gender, 
    level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE SET level = EXCLUDED.level
""")

song_table_insert = (""" 
INSERT INTO songs(
    song_id, 
    title, 
    artist_id, 
    year, 
    duration) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO NOTHING
""")

artist_table_insert = (""" 
INSERT INTO artists(
    artist_id, 
    artist_name, 
    artist_location, 
    artist_latitude, 
    artist_longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING
""")


time_table_insert = (""" 
INSERT INTO time(
    start_time, 
    hour, 
    day, 
    week, 
    month, 
    year, 
    weekday) VALUES(%s, %s, %s, %s, %s, %s, %s) ON CONFLICT (start_time) DO NOTHING
""")

# FIND SONGS
# find song_id and artist_id based on title, artist name, and duration of song.
# select timestamp, user_id, level, song_id, artist_id, session id, location, and user agent.

song_select = (""" 
    SELECT s.song_id, a.artist_id 
    FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id
    WHERE s.title = %s 
    AND a.artist_name = %s 
    AND s.duration = %s; """)

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
