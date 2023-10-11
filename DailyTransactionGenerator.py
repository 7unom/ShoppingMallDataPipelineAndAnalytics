import datetime
import pandas as pd
import numpy as np


# Sample product categories
product_categoryID = ["101", "102", "103", "104", "105"]

# Sample product IDs within each category
product_ids = {
    "101": [1, 2, 3, 24 ],
    "102": [4, 5, 6, 7],
    "103": [8, 9, 10, 11, 18, 19, 20, 23],
    "104": [12, 13, 14, 15],
    "105": [16, 17, 21, 22,]
}

# Create a list of customer IDs from 1 to 2000
customer_ids = list(range(1, 2001))  # Assumes a 2000 customer base

# Define fixed prices for each product ID
product_prices = {
    1: 999.99,
    2: 599.99,
    3: 799.99,
    4: 599.99,
    5: 43.99,
    6: 79.99,
    7: 1499.99,
    8: 14.99,
    9: 89.99,
    10: 19.99,
    11: 149.99,
    12: 79.99,
    13: 99.99,
    14: 99.99,
    15: 19.99,
    16: 69.99,
    17: 79.99,
    18: 39.99,
    19: 39.99,
    20: 29.99,
    21: 19.99,
    22: 199.99,
    23: 54.99,
    24: 129.99
}

# Define payment methods 
payment_methods = ["Cash", "Card"]


# Function to generate a random timestamp within a given date range
def generate_random_daily_timestamp():
    # Get the current date
    current_date = datetime.date.today()

    # Generate a random number of seconds within the current day
    random_seconds = np.random.randint(0, 86399)  # 86399 seconds in a day (0 to 23 hours, 59 minutes, 59 seconds)

    # Create a datetime object for the current date with the random time
    random_time = datetime.time(random_seconds // 3600, (random_seconds % 3600) // 60, random_seconds % 60)
    random_datetime = datetime.datetime.combine(current_date, random_time)

    return random_datetime


# Function to generate unique sales IDs
def generate_unique_sales_id():
    used_ids = set()
    for sales_id in range(1000, 9999):
        if sales_id not in used_ids:
            used_ids.add(sales_id)
            yield sales_id

# Create a generator for unique sales IDs
sales_id_generator = generate_unique_sales_id()


# Function to generate daily transactions
def generate_daily_transactions(num_transactions_per_day):
    transaction = []
    for _ in range(num_transactions_per_day):
        sales_id = next(sales_id_generator)
        customer_id = np.random.choice(customer_ids)
        category = np.random.choice(product_categoryID)
        product_id = np.random.choice(product_ids[category])
        if category == "101":
            quantity = np.random.randint(1, 2)
        elif category == "102":
            quantity = 1
        else:
            quantity = np.random.randint(1, 5)
        unit_price = product_prices.get(product_id, 0)  # Get the fixed unit_price for the product
        price = np.round(unit_price * quantity, decimals=2)
        payment_method = np.random.choice(payment_methods)
        timestamp = generate_random_daily_timestamp()

        # Create a dictionary for the current transaction
        transaction_data = {
            "Sales ID": sales_id,
            "Customer ID": customer_id,
            "Product ID": product_id,
            "Quantity": quantity,
            "Price": price,
            "Payment Method": payment_method,
            "DateTime": timestamp
        }

        transaction.append(transaction_data)

    # Create the DataFrame after the loop
    df = pd.DataFrame(transaction)
    return df


# Number of transactions to generate daily
min_target = 100
max_target = 1000
num_transactions_per_day = np.random.randint(min_target, max_target)

# Generate daily transactions and assign the DataFrame to a variable
df = generate_daily_transactions(num_transactions_per_day)

# sort transactions by date and sales ID
daily_transactions = df.sort_values(by=['DateTime', 'Sales ID'], ignore_index=True)
