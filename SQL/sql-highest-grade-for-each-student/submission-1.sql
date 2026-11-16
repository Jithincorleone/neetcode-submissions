-- -- Write your query below

-- with cte as 
-- (
-- select student_id,
--        exam_id,
--        score,
--        rank () over (partition by student_id order by score desc) rnk
-- from exam_results
-- ),
-- cte2 as 
-- (
-- select *,
-- rank() over (partition by student_id order by exam_id) rnk2
-- from cte
-- where rnk=1
-- )
-- select student_id, exam_id, score
-- from cte2
-- where rnk2=1;


SELECT DISTINCT ON (student_id)
    student_id,
    exam_id,
    score
FROM exam_results
ORDER BY student_id, score DESC, exam_id;