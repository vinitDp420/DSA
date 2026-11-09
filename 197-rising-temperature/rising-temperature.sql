# Write your MySQL query statement below
select w.id from Weather as w join Weather p
on DATEDIFF(w.recordDate , p.recordDate) = 1
where w.temperature > p.temperature;