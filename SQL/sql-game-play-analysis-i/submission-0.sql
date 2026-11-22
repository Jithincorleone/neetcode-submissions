-- Write your query below
select player_id,
event_date first_login
from
(
select *,
       row_number() over (partition by player_id order by event_date ) rnk
from activity
)
where rnk=1;