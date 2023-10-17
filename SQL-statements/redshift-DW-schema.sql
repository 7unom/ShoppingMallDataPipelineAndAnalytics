-- Create the retail_datawarehouse database
CREATE DATABASE retail_datawarehouse;

-- Create the Sales table
CREATE TABLE "public"."FactSales"(
    "sale_id" INTEGER NOT NULL,
    "customer_id" INTEGER NOT NULL,
    "product_id" INTEGER NOT NULL,
    "quantity" SMALLINT NOT NULL,
    "amount_paid" DECIMAL(10, 2) NOT NULL,
    "payment_method" VARCHAR(10) NOT NULL,
    "date_id" INTEGER NOT NULL,
    PRIMARY KEY("sale_id")
) ENCODE AUTO;

-- Create the Category table
CREATE TABLE "public"."DimCategory" (
    "category_id" SMALLINT NOT NULL,
    "category" VARCHAR(50) NOT NULL,
    PRIMARY KEY ("category_id")
) ENCODE AUTO;

-- Create the Product table
CREATE TABLE "public"."DimProduct" (
    "product_id" SMALLINT NOT NULL,
    "product_name" VARCHAR(50) NOT NULL,
    "description" CHARACTER VARYING(255),
    "selling_price" DECIMAL(10, 2) NOT NULL,
    "cost_price" DECIMAL NOT NULL,
    "category_id" SMALLINT NOT NULL,
    PRIMARY KEY ("product_id")
) ENCODE AUTO;

-- Create the Date Table
CREATE TABLE "public"."DimDate" (
    "date_id" INT,
    "sales_date" DATE NOT NULL,
    "year" SMALLINT,
    "quarter" SMALLINT,
    "quarter_name" VARCHAR(2),
    "month" SMALLINT,
    "month_name" VARCHAR(10),
    "day" SMALLINT,
    "weekday" SMALLINT,
    "weekday_name" VARCHAR(10),
    PRIMARY KEY ("date_id")
) ENCODE AUTO;


ALTER TABLE "public"."factsales"
    ADD FOREIGN KEY ("product_id")
    REFERENCES DimProduct ("product_id");

ALTER TABLE "public"."factsales"
        ADD FOREIGN KEY ("date_id")
    REFERENCES "dimdate" ("date_id");

ALTER TABLE "public"."dimproduct"
    ADD FOREIGN KEY ("category_id")
    REFERENCES "dimcategory" ("category_id");