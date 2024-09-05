CREATE DATABASE US_HOUSING_SALES;
USE US_HOUSING_SALES;

-- 1.SALE AS PER PRICE RANGE

SELECT `price_RANGE`,COUNT(count_no)
FROM `sales_data`
group by `price_RANGE`
order by COUNT(count_no) DESC;

-- 2.SALE AS PER `BEDROOM_RANGE`

SELECT `BEDROOM_RANGE`,COUNT(count_no)
FROM `sales_data`
group by `BEDROOM_RANGE`
order by COUNT(count_no) DESC;

-- 3.SALE AS PER `sqft_living_AREA`

SELECT `sqft_living_AREA`,COUNT(count_no)
FROM `sales_data`
group by `sqft_living_AREA`
order by COUNT(count_no) DESC;


-- 4.SALE AS PER sqft_lot_CATEGORICAL


SELECT sqft_lot_CATEGORICAL
,COUNT(count_no)
FROM `sales_data`
group by sqft_lot_CATEGORICAL
order by COUNT(count_no) DESC;


-- 5.SALE AS PER floors

SELECT `floors`,COUNT(count_no)
FROM `sales_data`
group by `floors`
order by COUNT(count_no) DESC;


-- 6.SALE AS PER `waterfront`

SELECT `waterfront`,COUNT(count_no)
FROM `sales_data`
group by `waterfront`
order by COUNT(count_no) DESC;

-- 7.SALE AS PER `view`

SELECT `view`,COUNT(count_no)
FROM `sales_data`
group by `view`
order by COUNT(count_no) DESC;

-- 8.SALE AS PER `condition`

SELECT `condition`,COUNT(count_no)
FROM `sales_data`
group by `condition`
order by COUNT(count_no) DESC;

-- 9.SALE AS PER `grade`

SELECT `grade`,COUNT(count_no)
FROM `sales_data`
group by `grade`
order by COUNT(count_no) DESC;

-- 10.SALE AS PER `sqft_above_CATEGORICAL`

SELECT `sqft_above_CATEGORICAL`,COUNT(count_no)
FROM `sales_data`
group by `sqft_above_CATEGORICAL`
order by COUNT(count_no) DESC;

-- 11.SALE AS PER `sqft_basement_CATEGORICAL`

SELECT `sqft_basement_CATEGORICAL`,COUNT(count_no)
FROM `sales_data`
group by `sqft_basement_CATEGORICAL`
order by COUNT(count_no) DESC;

-- 12 .SALE AS PER `yr_built_CATEGORICAL`

SELECT `yr_built_CATEGORICAL`,COUNT(count_no)
FROM `sales_data`
group by `yr_built_CATEGORICAL`
order by COUNT(count_no) DESC;

-- 13 .SALE AS PER `yr_renovated_CATEGORICAL`

SELECT `yr_renovated_CATEGORICAL`,COUNT(count_no)
FROM `sales_data`
group by `yr_renovated_CATEGORICAL`
order by COUNT(count_no) DESC;



















