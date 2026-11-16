-- Write your query below
with total_rides as
(
select user_id, sum(distance) total_distance
from rides   
group by user_id
)
select a.name, 
       case when b.total_distance is null then 0 else b.total_distance end as travelled_distance
from users a 
left join total_rides b
   on a.id=b.user_id
order by travelled_distance desc, a.name asc;
