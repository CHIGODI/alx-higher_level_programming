# SQL Introduction Project

## Overview
This project focuses on foundational SQL concepts and MySQL usage. It covers database creation, table manipulation, and basic queries. The tasks are designed to reinforce understanding of databases, SQL syntax, and practical application.

## Project Structure
The project is organized into several SQL scripts, each addressing a specific task. The scripts are numbered according to the corresponding task. Additionally, a brief description is provided for each task, guiding the user on the expected outcome.

## Getting Started
To execute the scripts, follow the instructions provided in each task. Ensure you have MySQL 8.0 installed on Ubuntu 20.04 LTS. Use allowed editors (vi, vim, emacs) and follow the conventions outlined in the project guidelines.

## Task Overview

### 0. List Databases
Script: [0-list_databases.sql](0x0D-SQL_introduction/0-list_databases.sql)
Description: Lists all databases on the MySQL server.

### 1. Create a Database
Script: [1-create_database_if_missing.sql](0x0D-SQL_introduction/1-create_database_if_missing.sql)
Description: Creates the database "hbtn_0c_0" if it doesn't exist.

### 2. Delete a Database
Script: [2-remove_database.sql](0x0D-SQL_introduction/2-remove_database.sql)
Description: Deletes the "hbtn_0c_0" database if it exists.

### 3. List Tables
Script: [3-list_tables.sql](0x0D-SQL_introduction/3-list_tables.sql)
Description: Lists all tables of a specified database.

### 4. First Table
Script: [4-first_table.sql](0x0D-SQL_introduction/4-first_table.sql)
Description: Creates a table called "first_table" in the current database.

### 5. Full Description
Script: [5-full_table.sql](0x0D-SQL_introduction/5-full_table.sql)
Description: Prints the full description of the "first_table" table.

### 6. List All in Table
Script: [6-list_values.sql](0x0D-SQL_introduction/6-list_values.sql)
Description: Lists all rows of the "first_table" table.

### 7. First Add
Script: [7-insert_value.sql](0x0D-SQL_introduction/7-insert_value.sql)
Description: Inserts a new row in the "first_table" table.

### 8. Count 89
Script: [8-count_89.sql](0x0D-SQL_introduction/8-count_89.sql)
Description: Displays the number of records with id = 89 in the "first_table" table.

### 9. Full Creation
Script: [9-full_creation.sql](0x0D-SQL_introduction/9-full_creation.sql)
Description: Creates a table "second_table" and adds multiple rows.

### 10. List by Best
Script: [10-top_score.sql](0x0D-SQL_introduction/10-top_score.sql)
Description: Lists all records of the "second_table" table, ordered by score.

### 11. Select the Best
Script: [11-best_score.sql](0x0D-SQL_introduction/11-best_score.sql)
Description: Lists records with a score >= 10 in the "second_table" table.

### 12. Cheating is Bad
Script: [12-no_cheating.sql](0x0D-SQL_introduction/12-no_cheating.sql)
Description: Updates the score of Bob to 10 in the "second_table" table.

### 13. Score Too Low
Script: [13-change_class.sql](0x0D-SQL_introduction/13-change_class.sql)
Description: Removes all records with a score <= 5 in the "second_table" table.

### 14. Average
Script: [14-average.sql](0x0D-SQL_introduction/14-average.sql)
Description: Computes the score average of all records in the "second_table" table.

### 15. Number by Score
Script: [15-groups.sql](0x0D-SQL_introduction/15-groups.sql)
Description: Lists the number of records with the same score in the "second_table" table.

### 16. Say My Name
Script: [16-no_link.sql](0x0D-SQL_introduction/16-no_link.sql)
Description: Lists all records of the "second_table" table, excluding rows without a name value.

### 17. Go to UTF8
Script: [100-move_to_utf8.sql](0x0D-SQL_introduction/100-move_to_utf8.sql)
Description: Converts the "hbtn_0c_0" database to UTF-8.

### 18. Temperatures #0
Script: [101-avg_temperatures.sql](0x0D-SQL_introduction/101-avg_temperatures.sql)
Description: Displays the average temperature by city ordered by temperature.

### 19. Temperatures #1
Script: [102-top_city.sql](0x0D-SQL_introduction/102-top_city.sql)
Description: Displays the top 3 cities' temperature during July and August ordered by temperature.

### 20. Temperatures #2
Script: [103-max_state.sql](0x0D-SQL_introduction/103-max_state.sql)
Description: Displays the max temperature of each state ordered by State name.
