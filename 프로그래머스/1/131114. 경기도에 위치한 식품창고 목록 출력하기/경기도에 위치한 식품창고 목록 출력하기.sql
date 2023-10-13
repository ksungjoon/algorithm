-- 코드를 입력하세요
SELECT WAREHOUSE_ID,WAREHOUSE_NAME,ADDRESS,IF(FREEZER_YN IS NULL, 'N',FREEZER_YN) AS FREEZER_YN 
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE '경기도%'
ORDER BY WAREHOUSE_ID ASC;