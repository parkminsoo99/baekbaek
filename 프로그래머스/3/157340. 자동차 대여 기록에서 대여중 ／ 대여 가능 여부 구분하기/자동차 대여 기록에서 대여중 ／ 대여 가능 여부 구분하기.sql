# -- 코드를 입력하세요
# # SELECT CAR_ID,
# #     CASE
# #         WHEN CAR_ID IN (select CAR_ID from CAR_RENTAL_COMPANY_RENTAL_HISTORY where '2022-10-16' between START_DATE and END_DATE) THEN '대여중'
# #         ELSE '대여 가능'
# #     END AS AVAILABILITY
# # from CAR_RENTAL_COMPANY_RENTAL_HISTORY group by Car_ID order by CAR_ID DESC

# select CAR_ID,
# CASE WHEN
# CAR_ID IN (
#     SELECT CAR_ID 
#     FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
#     WHERE '2022-10-16' between START_DATE and END_DATE
# )
# THEN
# '대여중'
# ELSE
# '대여 가능'
# END AS AVAILABILITY
# from CAR_RENTAL_COMPANY_RENTAL_HISTORY
# order by CAR_ID desc
# SELECT CAR_ID,
# CASE WHEN
# EXISTS (
#     SELECT 1 from CAR_RENTAL_COMPANY_RENTAL_HISTORY as c2
#     WHERE c1.CAR_ID = c2.CAR_ID
#     AND
#     '2022-10-16' between START_DATE and END_DATE
# )
# THEN '대여중'
# ELSE '대여 가능'
# END as AVAILABILITY
# FROM (SELECT distinct CAR_ID FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY) as c1
# order by CAR_ID desc


select 
CAR_ID,
case
when
CAR_ID IN 
(
    select CAR_ID 
    from CAR_RENTAL_COMPANY_RENTAL_HISTORY 
    where '2022-10-16' between START_DATE and END_DATE
)
then '대여중'
else '대여 가능'
end as AVAILABILITY
from
CAR_RENTAL_COMPANY_RENTAL_HISTORY
group by
CAR_ID
order by
CAR_ID desc