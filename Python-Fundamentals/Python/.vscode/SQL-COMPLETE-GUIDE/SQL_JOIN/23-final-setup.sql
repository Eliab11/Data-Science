 
CREATE TABLE projects(
    id SERIAL PRIMARY KEY, -- POstgresql
    title VARCHAR(300) NOT NULL,
    deadline DATE
 );
 
CREATE TABLE company_buildings(
    id SERIAL PRIMARY KEY , -- Postgresql
    name VARCHAR(300) NOT NULL
 );
CREATE TABLE teams(
    id SERIAL PRIMARY KEY, -- Postgresql
    name VARCHAR(300) NOT NULL,
    building_id INT REFERENCES company_buildings ON DELETE SET NULL
 ); 

CREATE TABLE employees (
    -- id INT PRIMARY KEY AUTO_INCREMENT, -- MySQl
    id SERIAL PRIMARY KEY, -- Postgres
    first_name VARCHAR(300) NOT NULL,
    last_name VARCHAR(300) NOT NULL,
    birthdate DATE NOT NULL,
    -- email VARCHAR(200)  REFERENCES intranet_accounts ON DELETE
    email VARCHAR(200) UNIQUE NOT NULL,
    team_id INT DEFAULT 1 REFERENCES teams ON DELETE SET NULL
);


CREATE TABLE intranet_accounts(
    --mid INT PRIMARY KEY AUTO_INCREMENT, --MySQl
    id SERIAL PRIMARY KEY, -- Postgresql
    email VARCHAR(200) REFERENCES employees(email) ON DELETE CASCADE, -- Postgresql
    -- email VARCHAR(200),
    -- FOREIGN key intranet_accounts(email) REFERENCES employees(email) ON DELETE CASCADE,
    password VARCHAR(200) NOT NULL 
);

-- Intermidiate table => n:n
CREATE TABLE projects_employees (
    id SERIAL PRIMARY KEY, -- Postgresql
    employee_id INT REFERENCES employees ON DELETE CASCADE,
    project_id INT REFERENCES  projects ON DELETE CASCADE
);

