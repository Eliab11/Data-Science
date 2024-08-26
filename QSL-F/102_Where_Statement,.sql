------------------------------------------------------------------------------------------------
-- PART 2: APPLYING CONDITIONS USING THE WHERE STATEMENT
------------------------------------------------------------------------------------------------

-- THE WHERE STATEMENT

select 
  *
from
 grocery_db.customer_details
;  


-- MULTIPLE CONDITIONS

-- and

select 
  *
from
 grocery_db.customer_details

where
 distance_from_store < 2 and 
 gender = 'M';  

-- or

select 
  *
from
 grocery_db.customer_details

where
 distance_from_store < 2 or 
 gender = 'M';
 
  
-- OTHER OPERATORS
/*
Equal to =
Not equal to <>
Greater than/Less than/Equal < > <=
 */
 
select 
  *
 
from 
  grocery_db.campaign_data;
 
-- in

select 
  *
 
from 
  grocery_db.campaign_data
 where 
 mailer_type in ('Mailer1', 'Mailer2');

-- like
select 
  *
 
from 
  grocery_db.campaign_data
 where 
 mailer_type like '%Mailer%';



select 
  customer_id,
  distance_from_store,
  gender
from grocery_db.customer_details

where distance_from_store <= 0.5 and
      gender in ('M', 'F') ;
   
