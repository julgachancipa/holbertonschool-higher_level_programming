-- creates the database hbtn_0d_usa
CREATE DATABASE  IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
-- creates the table cities on your MySQL server.
CREATE TABLE IF NOT EXISTS cities (
       id INT AUTO_INCREMENT NOT NULL,
       state_id INT NOT NULL,
       name VARCHAR(256) NOT NULL,
       PRIMARY KEY (id),
       FOREIGN KEY (state_id) REFERENCES states(id)
);
