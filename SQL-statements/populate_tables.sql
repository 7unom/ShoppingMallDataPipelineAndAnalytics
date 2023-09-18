-- Begin Code Snippet --
-- Code Explanation: The code snippet inserts data into two tables: 'category' and 'product'. 
-- It populates the 'category' table with category IDs and names, and the 'product' table with product details including product IDs, names, descriptions, unit prices, and category IDs.

-- Insert data into the 'category' table
INSERT INTO category(category_id, category)
VALUES
	(101, 'Electronics'),
    (102, 'Appliances'),
    (103, 'Clothings'),
    (104, 'Footwears'),
    (105, 'Accessories')
;

-- Insert data into the 'product' table
INSERT INTO product(product_id, product_name, description, unit_price, category_id)
VALUES
	(1, 'Laptop', 'High-performance laptop', 999.99, 101),
    (2, 'Smartphone', 'Latest smartphone model',  599.99, 101),
    (3, 'TV', ' 55-inch LED Smart TV', '799.99', 101),
    (4, 'Washing Machine', 'Front-Load Washing Machine', 599.99, 102),
    (5, 'Toaster', '4-Slice Toaster', 34.99, 102),
    (6, 'Microwave Oven', '1000W Countertop Microwave', 79.99, 102),
    (7, 'Refrigerator', '25 cu. ft. French Door Fridge', 1499.99, 102),
    (8, 'T-Shirt', 'Cotton T-shirt', 14.99, 103),
    (9, 'Dress', "Women's Evening Dress", 89.99, 103 ),
    (10, 'Polo shirts',	'Short-sleeved shirts with a collar and a few buttons at the neck',19.99, 103),  
    (11, 'Leather Jacket', "Men's Genuine Leather Jacket", 149.99, 103),
    (12, 'Running Shoes', 'unisex running shoes', 79.99, 104),
    (13, 'Dress shoes',	'Shoes designed for formal occasions', 99.99, 104),
    (14, 'Casual shoes', 'Shoes designed for everyday wear', 39.99, 104),
    (15, 'Slippers',	'Comfortable shoes designed to be worn indoors', 19.99, 104),
    (16, 'Backpack', 'Waterproof Backpack', 69.99, 105),
    (17, "Watches", 'Timepieces worn on the wrist.', 79.99, 105),
    (18, 'Skirts',	'Dresses without sleeves', 39.99, 103),
    (19, 'Jeans',	'Denim pants',39.99, 103),
    (20, 'Shorts',	'Short pants', 29.99, 103),
    (21, 'Sunglasses', "Eyewear that protects the eyes from the sun's harmful UV rays",	19.99, 105),
    (22, 'Jewelry',	'Decorative items worn on the body, such as necklaces, earrings, and bracelets', 109.99, 105),
    (23, 'Button-down shirt', 'Long-sleeved shirts with buttons down the front', 24.99, 103),
    (24, 'Headphones', 'Noise-canceling headphones', 129.99, 101)
;
-- End Code Snippet --