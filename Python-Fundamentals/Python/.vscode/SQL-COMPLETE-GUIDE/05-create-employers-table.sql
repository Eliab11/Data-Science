DROP TABLE employers;
CREATE TABLE employers(
    company_name VARCHAR(250),
    company_addres VARCHAR(300),
   -- yearly_revenue FLOAT(5,2) --Approximation, Allowed: 123.12, 12.1
   yearly_revenue NUMERIC(5,2), -- Exact value, Allowed: 123.12, Not 
   is_hiring BOOLEAN
);