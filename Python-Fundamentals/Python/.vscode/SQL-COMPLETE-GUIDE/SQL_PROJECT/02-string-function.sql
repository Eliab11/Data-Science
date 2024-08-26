-- SELECT CONCAT(first_name, ' ', last_name)
-- FROM memberships;

-- SELECT first_name || ' ' || last_name
-- FROM memberships;

-- SELECT CONCAT('$ ', price)
-- FROM memberships;

-- SELECT * FROM memberships
-- WHERE LENGTH(last_name) < 7;

-- DOW postgresSQL only
-- SELECT EXTRACT(DOW FROM last_checkin), last_checkin
-- FROM memberships;

-- SELECT WEEKDAY(last_checkin) + 1, last_checkin
-- FROM memberships;

-- SELECT last_checkout - last_checkin
-- FROM memberships;

SELECT first_name LIKE '%u%', first_name
FROM memberships;