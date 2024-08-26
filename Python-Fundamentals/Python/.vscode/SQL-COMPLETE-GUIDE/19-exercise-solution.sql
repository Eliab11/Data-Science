-- Task 1: Create Database

-- CREATE DATABASE online_shop;

-- -- Tasks 2 + 3: Create and configure table

-- CREATE TABLE  products(
--     name VARCHAR(200),
--     price NUMERIC(10,2), -- 8.99, 12345.99
--     description TEXT,
--     amounts_in_stock SMALLINT,
--     image_path VARCHAR(500) -- 'uploads/images/products/some-product.jpg'
-- );


-- INSERT INTO products(price, name, description, amounts_in_stock, image_path)
-- VALUES (12.99, 'A Book',
-- 'This is a book - and this text could be way longer!',
-- 39,
-- 'uploads/images/products/some-product.jpg'
-- );

-- Tasks 5: Add constraints
 
MODIFY COLUMN name VARCHAR(200) NOT NULL,
MODIFY COLUMN price NUMERIC(10,2) NOT NULL CHECK(pricec > 0),
MODIFY COLUMN description TEXT NOT NULL,
MODIFY COLUMN amounts_in_stock SMALLINT CHECK (amounts_in_stock >= 0);