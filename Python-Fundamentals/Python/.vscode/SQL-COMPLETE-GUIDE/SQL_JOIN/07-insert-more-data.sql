SELECT c.name AS city_name
FROM cities AS c 
INNER JOIN addresses AS a ON c.id = a.city_id; 