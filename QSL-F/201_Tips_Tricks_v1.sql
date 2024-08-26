-------------------------------------------------------------------------------------------------------
-- USEFUL TIPS & TRICKS (VOLUME 1)
-------------------------------------------------------------------------------------------------------



----------------------------------------------------------
-- Using Sub-Queries
----------------------------------------------------------


select 
   product_area_name,
   profit_margin
   
from
   
   grocery_db.product_areas
   

where 
    -- profit_margin = (select max(profit_margin) from grocery_db.product_areas);
    

------------------------------------------------------------------------------------------------------------------
-- Using Lead & Lag
------------------------------------------------------------------------------------------------------------------


create temp table cust_trans as (
select 
   distinct customer_id,
   transaction_id,
   transaction_date


from 
   grocery_db.transactions
   
where 
   customer_id in (1,2)
   );
   
select  
 *,
 lag(transaction_date, 1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag1,
 lag(transaction_date, 2) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lag2,
 lead(transaction_date, 1) over (partition by customer_id order by transaction_date, transaction_id) as transaction_date_lead1
 
from 
   cust_trans;
   
--------------------------------------------------------------------------------------------------------------------------------
-- Rounding Data
--------------------------------------------------------------------------------------------------------------------------------

select 
*,
     
