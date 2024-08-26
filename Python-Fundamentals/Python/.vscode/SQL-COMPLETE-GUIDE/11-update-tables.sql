ALTER TABLE employers
ALTER COLUMN yearly_revenue SET DATA TYPE FLOAT;  -- Postgresql

ALTER TABLE employers
MODIFY COLUMN yearly_revenue FLOAT(5,2); --MySQL


