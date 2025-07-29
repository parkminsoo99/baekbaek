-- 코드를 입력하세요
# SET @TIME = -1;
# SELECT (@TIME := @TIME+1) AS HOUR,
# (select COUNT(HOUR(DATETIME)) from ANIMAL_OUTS where HOUR(DATETIME) = @TIME) AS COUNT
# from ANIMAL_OUTS
# where @TIME < 23
# SET @TIME = -1;
# SELECT 
# (@TIME := @TIME +1) as HOUR,
# (
#     SELECT COUNT(ANIMAL_ID) 
#     from ANIMAL_OUTS
#     WHERE HOUR(DATETIME) = @TIME
# ) as COUNT
# FROM ANIMAL_OUTS
# WHERE @TIME < 23;

with recursive test as (
select 0 as hour 
    union all
select hour+1 from test where hour<23
)
select hour as HOUR, count(a.ANIMAL_ID) as COUNT 
from test t left join ANIMAL_OUTS a on t.hour = HOUR(a.DATETIME)
group by t.hour
order by t.hour