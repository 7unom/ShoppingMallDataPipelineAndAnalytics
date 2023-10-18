SELECT
    sale_id,
    customer_id,
    product_id,
    quantity,
    amount_paid,
    payment_method,
    dd.date_id
FROM transactions s
JOIN dim_date dd ON CAST(s.timestamp AS DATE) = dd.sales_date;
