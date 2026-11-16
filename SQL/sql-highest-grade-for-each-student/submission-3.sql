-- -- Write your query below

with cte as 
(
select student_id,
       exam_id,
       score,
       rank () over (partition by student_id order by score desc, exam_id asc) rnk
from exam_results
)
select student_id, exam_id, score
from cte
where rnk=1;


-- SELECT DISTINCT ON (student_id)
--     student_id,
--     exam_id,
--     score
-- FROM exam_results
-- ORDER BY student_id, score DESC, exam_id;