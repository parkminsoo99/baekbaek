# SELECT ranked.FOOD_TYPE,ranked.REST_ID,ranked.REST_NAME,ranked.FAVORITES
# FROM
# (
#     SELECT
#     *,RANK() OVER(PARTITION BY FOOD_TYPE ORDER BY FAVORITES DESC) AS R
#     FROM
#     REST_INFO
# ) ranked
# WHERE
# ranked.R = 1
# order by
# ranked.FOOD_TYPE DESC


# select 
# FOOD_TYPE,REST_ID,REST_NAME,FAVORITES 
# from 
# (
# select *, rank() over(partition by FOOD_TYPE order by FAVORITES DESC ) as R from REST_INFO
# ) as ranked
# where ranked.R = 1
# order by FOOD_TYPE DESC

select
FOOD_TYPE,REST_ID,REST_NAME,FAVORITES
from
(
    select 
    *, RANK() over(partition by FOOD_TYPE order by FAVORITES desc) as ranked
    from
    REST_INFO
) as rank_table
where ranked = 1
# group by
# FOOD_TYPE
order by
FOOD_TYPE desc 

