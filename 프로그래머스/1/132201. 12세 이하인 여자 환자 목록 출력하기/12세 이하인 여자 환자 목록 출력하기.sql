# -- 코드를 입력하세요
# # SELECT PT_NAME,PT_NO, GEND_CD, AGE, COALESCE(TLNO,'NONE') as TLNO from PATIENT where GEND_CD = 'W' and age <= 12 order by age DESC, PT_NAME ASC


# select PT_NAME, PT_NO, GEND_CD, AGE, coalesce(TLNO,'NONE') as TLNO from PATIENT where AGE <= 12 and GEND_CD = 'W' order by age desc, PT_NAME asc


select PT_NAME, PT_NO, GEND_CD, AGE,
case
when TLNO is null
then 'NONE'
else TLNO
end as TLNO
from PATIENT
where age <=12 and gend_cd = 'W'
order by age desc, PT_NAME asc