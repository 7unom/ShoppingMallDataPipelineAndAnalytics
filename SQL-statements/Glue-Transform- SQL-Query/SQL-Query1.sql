SELECT
  DENSE_RANK() OVER (ORDER BY CAST(sales_date AS DATE)) AS date_id,
  CAST(sales_date AS DATE) AS sales_date,
  YEAR(sales_date) AS year,
  QUARTER(sales_date) AS quarter,
  CASE
    WHEN QUARTER(sales_date) = 1 THEN 'Q1'
    WHEN QUARTER(sales_date) = 2 THEN 'Q2'
    WHEN QUARTER(sales_date) = 3 THEN 'Q3'
    WHEN QUARTER(sales_date) = 4 THEN 'Q4'
    ELSE NULL
  END AS quarter_name,
  MONTH(sales_date) AS month,
  DATE_FORMAT(sales_date, 'MMMM') AS month_name,
  DAY(sales_date) AS day,
  DAYOFWEEK(sales_date) AS weekday,
  DATE_FORMAT(sales_date, 'EEEE') AS weekday_name
FROM (
  SELECT DISTINCT
    CAST(timestamp AS DATE) AS sales_date
  FROM transactions
) t;