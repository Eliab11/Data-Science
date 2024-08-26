------------------------------------------------------------------------------------------------------
-- WINDOW FUNCTIONS
------------------------------------------------------------------------------------------------------

-- WINDOW FUNCTION

select 
*,
sum(sales_cost) over(partition by transaction_id) as transaction_total_sales,
sales_cost / sum(sales_cost) over(partition by transaction_id) as transaction_sales_percent

from
   grocery_db.transactions;
   
-- ROW NUMBER & RANK

select 
   *,
   row_number() over (partition by customer_id order by transaction_date, transaction_id) as transaction_sales_poercent
   
from
   grocery_db.transactions;
   




select 
    customer_id,
    gender,
    distance_from_store,
    rank() over(partition by gender order by distance_from_store) as distance_from_store_rank
    
from
  grocery_db.customer_details
  
where 
  gender in ('M', 'F') and
  distance_from_store is not null;

