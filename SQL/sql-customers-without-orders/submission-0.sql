-- Write your query below
select name
from customers a
where not exists (select 1
                  from orders b
                  where a.id = b.customer_id);