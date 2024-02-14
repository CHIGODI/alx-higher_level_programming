-- creates the database hbtn_0d_usa and the table states

-- create DB
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- creates table in above DB
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
       id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
       name VARCHAR(256)
);
