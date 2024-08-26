select 
    customer_id

from  
    grocery_db.customer_details


where 
    distance_from_store = (select min(distance_from_store) from grocery_db.customer_details order by distance_from_store desc) ;
