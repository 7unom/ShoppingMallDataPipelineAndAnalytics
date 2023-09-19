"""
Generates historical transactions by randomly selecting customer IDs, product categories, product IDs, quantities, and timestamps. Calculates the total amount for each transaction based on the fixed prices of the products. Stores the transactions in a pandas DataFrame and sorts them by timestamp and sales ID.

Inputs:
- product_categories: A list of product categories.
- product_ids: A dictionary mapping each product category to a list of product IDs within that category.
- customer_ids: A list of customer IDs.
- product_prices: A dictionary mapping each product ID to its fixed price.
- num_historical_transactions: The number of historical transactions to generate per day.

Outputs:
- Sorted DataFrame containing the historical transactions, with columns for sales ID, customer ID, category, product ID, quantity, unit price, sales amount, and timestamp.
"""


import random
import datetime
import pandas as pd

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


def generate_random_timestamp():
    """
    Generates a random timestamp within a specified date range.

    This function generates a random timestamp that falls within the date range
    between January 1, 2023, and December 31, 2023, inclusive. The generated
    timestamp includes both a random date and a random time of day.

    Returns:
    - datetime.datetime: A random timestamp within the specified date range.
    >>> 2023-06-15 14:32:55

    Explanation of the code:
    - The function calculates the total number of seconds within the date range,
      selects a random number of days and random seconds within that range,
      and then creates a random timestamp using the selected values.
    """
    # Define the start and end dates for the date range
    start_date = datetime.datetime(2023, 1, 1)
    end_date = datetime.datetime(2023, 12, 31)

    # Calculate the duration (delta) between the start and end dates
    delta = end_date - start_date

    # Generate a random number of days within the entire date range
    random_days = random.randint(0, delta.days)
    
    # Generate a random number of seconds within the current day
    random_seconds = random.randint(0, 86399)  # 86399 seconds in a day (0 to 23 hours, 59 minutes, 59 seconds)

    # Create a datetime object for the current date with the random time
    random_datetime = start_date + datetime.timedelta(days=random_days, seconds=random_seconds)

    return random_datetime


def generate_historical_transactions(num_historical_transactions):
    """
    Generates a specified number of historical transactions per day.

    Args:
        num_historical_transactions (int): The number of historical transactions to generate.

    Returns:
        None. The generated transactions are stored in the global DataFrame `df`.

    Code Analysis:
        - Initialize an empty list to store the transactions.
        - For each transaction to be generated:
            - Generate a random sales ID between 1000 and 9999.
            - Select a random customer ID from the given list of customer IDs.
            - Select a random product category from the given list of product categories.
            - Select a random product ID within the selected category.
            - Generate a random quantity between 1 and 5 except for products in category 102(between 1 and 2).
            - Get the fixed price of the selected product ID.
            - Calculate the sales amount by multiplying the unit price with the quantity.
            - Generate a random timestamp within the specified date range.
            - Create a dictionary with the transaction data.
            - Append the transaction data dictionary to the list of transactions.
        - Create a pandas DataFrame from the list of transactions.
        - Make the DataFrame global.
    """
    transactions = []
    for _ in range(num_historical_transactions):
        sales_id = random.randint(1000, 9999)
        customer_id = random.choice(customer_ids)
        category = random.choice(product_categoryID)
        product_id = random.choice(product_ids[category])

        # Determine the quantity of the product based on product category
        if category == "102":
            quantity = random.randint(1, 2)
        elif category == "101":
            quantity = 1
        else:
            quantity = random.randint(1, 5)
        unit_price = product_prices.get(product_id, 0)  # Get the fixed price for the product
        sales_amount = unit_price * quantity
        timestamp = generate_random_timestamp()

        # Create a dictionary for the current transaction
        transaction_data = {
            "Sales ID": sales_id,
            "Customer ID": customer_id,
            # "Category": category,
            "Product ID": product_id,
            "Quantity": quantity,
            # "Unit Price": unit_price,
            "Sales Amount": sales_amount,
            "DateTime": timestamp
        }

        transactions.append(transaction_data)

    global df  # make df global
    df = pd.DataFrame(transactions)

# Number of historical transactions to generate 
num_historical_transactions = 500 # target number should be >= 500000

# Generate historical transactions
generate_historical_transactions(num_historical_transactions)

# Print the DataFrame with all transactions
df_sorted = df.sort_values(by=['DateTime', 'Sales ID'], ignore_index=True)
print(df_sorted)