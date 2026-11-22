-- Write your query below
with host_teams_points as
(
select mt.host_team as team_id,
      case when mt.host_goals > mt.guest_goals then 3
           when mt.host_goals = mt.guest_goals then 1
           when mt.host_goals < mt.guest_goals then 0
      end as points
from matches mt
),
guest_teams_points as
(
select mt.guest_team as team_id,
      case when mt.guest_goals > mt.host_goals then 3
           when mt.guest_goals = mt.host_goals then 1
           when mt.guest_goals < mt.host_goals then 0
      end as points
from matches mt
),
combined_points as
(
    select * from host_teams_points
    union all 
    select * from guest_teams_points
)
select tm.team_id, tm.team_name, sum(case when points is null then 0 else points end) num_points
from teams tm
  left outer join combined_points cp
    on tm.team_id = cp.team_id
group by tm.team_id, tm.team_name
order by num_points desc, tm.team_id asc;