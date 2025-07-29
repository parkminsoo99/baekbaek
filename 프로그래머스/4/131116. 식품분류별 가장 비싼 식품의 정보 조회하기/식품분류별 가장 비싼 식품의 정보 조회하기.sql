-- 코드를 입력하세요
# SELECT CATEGORY, 
# PRICE AS MAX_PRICE, PRODUCT_NAME 
# FROM FOOD_PRODUCT
# where (CATEGORY, PRICE) IN (select CATEGORY, MAX(PRICE) from FOOD_PRODUCT where CATEGORY IN ('과자', '국', '김치', '식용유') group by CATEGORY )
# order by PRICE DESC

select 
CATEGORY, PRICE as MAX_PRICE,PRODUCT_NAME
from 
FOOD_PRODUCT
where (CATEGORY,PRICE) IN (
    select 
    CATEGORY,max(PRICE) 
    from 
    FOOD_PRODUCT 
    group by CATEGORY
)
and CATEGORY REGEXP '과자|국|김치|식용유'
group by
PRODUCT_NAME
order by 
MAX_PRICE desc
