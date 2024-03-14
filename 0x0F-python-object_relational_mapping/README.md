# Object-Relational Mapping Project

This repository contains Python scripts developed as part of the Object-Relational Mapping (ORM) project, focusing on linking databases and Python using modules such as MySQLdb and SQLAlchemy. The project covers various tasks aimed at connecting to a MySQL database, executing SQL queries, working with ORM, and performing CRUD operations.

## Project Structure

The project is organized into the following directories:

- **0x0F-python-object_relational_mapping**: Contains Python scripts for different tasks related to ORM.
- **model_state.py**: Defines the class `State` and an instance `Base` using SQLAlchemy.
- **model_city.py**: Defines the class `City` using SQLAlchemy, inheriting from `Base`.

## Tasks Overview

The tasks covered in this project include:

- **0-select_states.py**: Script to list all states from the database `hbtn_0e_0_usa`.
- **1-filter_states.py**: Script to list all states with a name starting with "N" from the database `hbtn_0e_0_usa`.
- **2-my_filter_states.py**: Script that takes an argument and lists all states matching the argument from the database `hbtn_0e_0_usa`.
- **3-my_safe_filter_states.py**: Script similar to `2-my_filter_states.py` but protects against SQL injection.
- **4-cities_by_state.py**: Script that lists all cities from the database `hbtn_0e_4_usa` ordered by `city.id`.
- **5-filter_cities.py**: Script that takes the name of a state as an argument and lists all cities of that state from the database `hbtn_0e_4_usa`.
- **6-model_state.py**: Script that prints the first `State` object from the database `hbtn_0e_6_usa`.
- **7-model_state_fetch_all.py**: Script that lists all `State` objects from the database `hbtn_0e_6_usa`.
- **8-model_state_fetch_first.py**: Script that prints the `State` object with the `id` passed as an argument from the database `hbtn_0e_6_usa`.
- **9-model_state_filter_a.py**: Script that lists all `State` objects containing the letter 'a' from the database `hbtn_0e_6_usa`.
- **10-model_state_my_get.py**: Script that prints the `State` object with the name passed as an argument from the database `hbtn_0e_6_usa`.
- **11-model_state_insert.py**: Script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
- **12-model_state_update_id_2.py**: Script that changes the name of a `State` object from the database `hbtn_0e_6_usa`.
- **13-model_state_delete_a.py**: Script that deletes all `State` objects with a name containing the letter 'a' from the database `hbtn_0e_6_usa`.
- **model_state.py**: Python file defining the class `State` and an instance `Base` using SQLAlchemy.
- **model_city.py**: Python file defining the class `City` using SQLAlchemy, inheriting from `Base`.

## How to Use
For example:

```bash
./0-select_states.py root root hbtn_0e_0_usa
