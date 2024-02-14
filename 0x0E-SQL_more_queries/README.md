0x0E-SQL_more_queries
Overview
This repository contains a series of SQL scripts designed to help you practice and reinforce your skills in working with MySQL databases. The tasks cover various aspects, from user privileges to database table creation and complex queries.

<h2>Tasks</h2>
The project is organized as follows:

0-privileges.sql: Lists privileges of MySQL users.
1-create_user.sql: Creates a MySQL user with all privileges.
2-create_read_user.sql: Creates a database and user with SELECT privilege.
3-force_name.sql: Creates a table with a non-nullable name column.
4-never_empty.sql: Creates a table with a default value for the id column.
5-unique_id.sql: Creates a table with a unique id column.
6-states.sql: Creates a database and a states table.
7-cities.sql: Creates a database and a cities table with a foreign key constraint.
8-cities_of_california_subquery.sql: Lists cities in California without using JOIN.
9-cities_by_state_join.sql: Lists all cities and states using JOIN.
10-genre_id_by_show.sql: Lists TV show names with their associated genre.
11-genre_id_all_shows.sql: Lists all genres and the names of the shows under each genre.
12-no_genre.sql: Lists shows that do not have a genre.
13-count_shows_by_genre.sql: Lists the number of shows in each genre.
14-my_genres.sql: Uses a temporary table to list all genres of a specific user.
15-comedy_only.sql: Lists comedy shows with their name and genre.
16-shows_by_genre.sql: Lists shows and their genres alphabetically.
17-not_my_genre.sql: Lists shows that are not of a specified genre.
18-not_a_comedy.sql: Lists shows that are not in the comedy genre and their genres.
19-no_comedy.sql: Deletes all shows that are in the comedy genre.