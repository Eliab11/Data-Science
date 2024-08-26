
CREATE TABLE employees (
    -- id INT PRIMARY KEY AUTO_INCREMENT, -- MySQl
    id SERIAL PRIMARY KEY, -- Postgres
    first_name VARCHAR(300) NOT NULL,
    last_name VARCHAR(300) NOT NULL,
    birthdate DATE NOT NULL,
    -- email VARCHAR(200)  REFERENCES intranet_accounts ON DELETE
    email VARCHAR(200) UNIQUE NOT NULL
);


CREATE TABLE intranet_accounts(
    --mid INT PRIMARY KEY AUTO_INCREMENT, --MySQl
    id SERIAL PRIMARY KEY, -- Postgresql
    email VARCHAR(200) REFERENCES employees (email) ON DELETE CASCADE, -- Postgresql
    -- email VARCHAR(200),
    -- FOREIGN key intranet_accounts(email) REFERENCES employees(email) ON DELETE CASCADE,
    password VARCHAR(200) NOT NULL 
);