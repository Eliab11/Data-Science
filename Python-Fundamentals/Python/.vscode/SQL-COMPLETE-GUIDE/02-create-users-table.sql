
-- Postgressql + ENUM => We have to create a custom type first
CREATE TYPE employment_status_1 AS ENUM('emplyed','self-employed','unemployed');

 CREATE TABLE users(
   full_name VARCHAR(200),
   yearly_salary INT,
   current_status employment_status_1
   -- current_status ENUM('emplyed','self-employed','unemployed')
 );