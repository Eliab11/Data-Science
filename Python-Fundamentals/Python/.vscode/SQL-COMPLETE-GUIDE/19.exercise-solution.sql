-- task 1: Create database

-- CREATE DATABASE online_shop;

-- Task 2 + 3 : Create and configure table
-- CREATE TABLE products(
--     name VARCHAR(200),
--     price NUMERIC(10,2),-- 0.899, 12345.99 
--     description TEXT,
--     amount_in_stock SMALLINT,
--     image_path VARCHAR(500) -- 'uploads/images/products/some-product.jpg'

-- );
-- 
-- SELECT * FROM products;

ALTER TABLE products
MODIFY COLUMN name VARCHAR(200) NOT NULL,
MODIFY COLUMN price NUMERIC(10,2) NOT NULL CHECK (price > 0),
MODIFY COLUMN description TEXT NOT NULL,
MODIFY COLUMN amount_in_stock SMALLINT CHECK (amount_in_stock >= 0
);