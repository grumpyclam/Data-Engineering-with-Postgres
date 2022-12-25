# Introduction
>
 A startup called Sparkify has been collecting data on the songs and users for their new music streaming app. The analytics team wants to analyze what the users are listening to but they currenty don't have a way to query the data. The data resides in sperate JSON directory files for both users and song data. The JSON data for users collectes logs about what users are doing, and the JSON file for songs collects metadata associated with each song.
>
Sparkify needs a data engineer to create a database with Postgres so that queries can be optimized for song play analysis. The goal is to create a database schema and ETL pipeline. The files used in the project as well as the schema and tables created are listed below.
> 
>
# Files used in this project. 
>
**sql_queries.py**
>
> - This is where all sql create and insert statements, song joins and table queries are stored. These statements are imported into create_tables.py, etl.ipynb and etl.py.
>
**create_tables.py**
>
> - This is a function that is written to actually create, drop, and insert the tables created in sql_queries.py. This file has to be run before etl.ipynb will work and if any changes are made on sql_queries, it must be run again. It's advised that if any changes are made that you shutdown all kernels and start again.
>
**etl.ipynb**
>
> - This is the file that is used to develop the ETL process for only single rows (song and log data) with the tables and insert statements that were used in sql_queries.py. Create_tables.py must be run before this file will work.
>
**etl.py**
>
> - This file is used to read and process the song and log data that we used in etl.ipynb. It imports all of the information from song and log data instead of a single row (like etl.ipynb). It is very similar to etl.ipynb.
>
**test.ipynb**
>
> - This file must be run after code is run in etl.ipynb to make sure that that data you're extracting and inserting is actually working. Again, the kernel will need to be shutdown and run again after every script run.
>
>
# How to run the files:
> 
You should run the following files in this order:
> 1. sql_queries.py
This is the base file that contains all the sql queries. If you'd like to make changes to the database (create/insert) statements this is where you would do it.
> 2. create_tables.py
This function runs all the code you made in sql_queries.py and creates the tables. You can run this with a simple (!python create_tables.py) in the console.
> 3. etl.ipynb
Jupyter notebook that allows you to visualize the ETL proccess of extracting and inserting of files.
> 4. test.ipynb
Run this after running etl.ipynb to make sure the the etl process is working, will allow you to visualize what you've done.
> 4. etl.py
Allows to read and process the log and song data associated with etl.ipynb.
>
# Tables and Schema
>
I chose to use the star schema for this project because there is one fact table (songplays) and four dimension tables around it that are related via primary key. I also chose to use the star schema because it simplifies queries and aggregations are fast. Tables are listed below.
>
**Fact Table**
>
- Records in log data associated with song plays i.e. records with page NextSong.
>
- songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent
>
**Dimension Tables**
>
- **users:** users in the app. (user_id, first_name, last_name, gender, level)
>
- **songs:** songs in music database. (song_id, title, artist_id, year, duration)
>

- **artists:** artists in music database. (artist_id, name, location, latitude, longitude)
>
- **time** timestamps of records in songplays broken down into specific units. ( start_time, hour, day, week, month, year, weekday
