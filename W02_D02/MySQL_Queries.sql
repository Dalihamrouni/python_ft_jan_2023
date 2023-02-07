# CRUD
# acronym that describes EVERYTHING we can do with data EVER
# CREATE
# MySQL command: INSERT
# SQL Syntax: INSERT INTO table_name (column1, column2) VALUES (value1, value2);
--  SET SQL_SAFE_UPDATES = 0;
  
 -- INSERT One
 -- #With id  :  Auto incremanted
 -- #With created_at & updated_at as default values
 INSERT INTO users (first_name, last_name, email) VALUES ('John', 'Wick', 'jw@email.com');
 
 -- INSERT Many
 INSERT INTO users (first_name, last_name,email) VALUES  ('Max', 'Taylor', 'mt@email.com'), ('Jack', 'Stones', 'js@email.com');
INSERT INTO users (first_name, last_name,email) VALUES  ('Alex', 'Jones', 'mt@email.com'), ('Mary', 'Ryan', 'js@email.com');

-- One To One
 INSERT INTO   adresses (street, city, state, zip_code) VALUES ('Number One', 'NY', 'State 1 ','1234')

-- # READ
-- # MySQL command : SELECT
-- # SQL Snytax : SELECT (columns names that i need to grab) FROM table_name;

-- Select all the users
 SELECT * FROM users;
 -- # I want to add a condition
 SELECT * FROM users WHERE id = 3;
 
 SELECT first_name, last_name FROM users WHERE id = 3;
 -- # Select the same first_name

 SELECT first_name, last_name FROM users WHERE first_name = "Max";
 -- # Select all first_names starting with M

SELECT * FROM users WHERE first_name LIKE 'J%';
-- # Sorting

SELECT * FROM users ORDER BY id  ASC;
SELECT * FROM users ORDER BY id  DESC;


SELECT * FROM users ORDER BY id DESC LIMIT 2;
  
SELECT * FROM users WHERE id  > 3;

-- # UPDATE 
-- # MySQL command : UPDATE
-- # SQL Snytax : UPDATE table_name SET column_1 = value1 , column_2 = value2 WHERE condition;

 UPDATE users SET first_name  = 'Sarah', email = 'sw@email.com';
 
-- # DELETE
-- # MySQL command : DELETE
-- # SQL Snytax : DELETE FROM table_name WHERE condition;
DELETE FROM users WHERE id = 2;
DELETE * FROM users;
-- Functions 
SELECT CONCAT(first_name, last_name, email) AS fullname FROM users;
SELECT CONCAT_WS('--',first_name, last_name, email) AS fullname FROM users;

