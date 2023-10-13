-- Start of SQL Script

-- Description: This SQL script creates a database and table for retail transactions in an OLTP system.

-- Create a new database named 'retail_db' if it doesn't exist.
CREATE DATABASE IF NOT EXISTS retail_db;

-- Use the 'retail_db' database for subsequent commands.
USE retail_db;

-- Create a 'transactions' table for retail transactions.
-- This table is designed for OLTP (Online Transaction Processing) purposes.
CREATE TABLE transactions (
    sale_id SERIAL PRIMARY KEY,          -- Unique identifier for each sale
    customer_id INT NOT NULL,            -- Customer ID associated with the sale
    product_id SMALLINT NOT NULL,        -- Product ID associated with the sale
    quantity SMALLINT NOT NULL,         -- Quantity of products sold
    amount_paid NUMERIC(10, 2),         -- Amount paid for the sale
    payment_method VARCHAR(10),         -- Payment method used
    timestamp TIMESTAMP                  -- Timestamp of the transaction
);

-- End of SQL Script
