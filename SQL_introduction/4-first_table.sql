-- script that creates a table called first_table in the current database in the MySQL server
CREATE DATABASE hbtn_0c_0;

-- Select the database
USE hbtn_0c_0;

-- Create a table in the database 
CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
);
