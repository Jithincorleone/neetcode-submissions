-- Write your query below
-- select *
-- from customers 
-- where 1=1
--   and customer_id in (select customer_id from orders where product_name = 'A')
--   and customer_id in (select customer_id from orders where product_name = 'B')
--   and customer_id not in (select customer_id from orders where product_name = 'C')
-- order by customer_id;

select *
from customers 
where customer_id in 
(
select customer_id
from orders a
group by customer_id
having sum(case when product_name = 'A' then 1 else 0 end) > 0
   and sum(case when product_name = 'B' then 1 else 0 end) > 0
   and sum(case when product_name = 'C' then 1 else 0 end) = 0
)
order by customer_name;