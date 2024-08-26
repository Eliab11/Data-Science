-- INSERT INTO sales(
--     customer_name,
--     product_name,
--     volume,
--     is_recurring
-- )
-- VALUES(
--     'Mar Schwarz',
--     'A Book',
--     12.99,
--     TRUE
-- )

INSERT INTO sales(
    date_fulfilled,
    customer_name,
    product_name,
    volume,
    is_recurring,
    is_disputed
)
VALUES(
    NULL,
    'Learning Inc',
    'Course Bundle',
    4889.62,
    FALSE,
    FALSE
), (
    NULL,
    '2022-04-10',
    'Big Oil Inc',
    400000.0,
    FALSE,
    TRUE
);
