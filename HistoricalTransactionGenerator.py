"""
Generates historical transactions by randomly selecting customer IDs,
product categories, product IDs, quantities, and timestamps. 
Calculates the total amount for each transaction based on the fixed prices of the products.
 Stores the transactions in a pandas DataFrame and sorts them by timestamp and sales ID.

Inputs:
- product_categories: A list of product categories.
- product_ids: A dictionary mapping each product category to a list of product IDs within that category.
- customer_ids: A list of customer IDs.
- product_prices: A dictionary mapping each product ID to its fixed price.
- num_historical_transactions: The number of historical transactions to generate per day.

Outputs:
- Sorted DataFrame containing the historical transactions, with columns for sales ID, 
customer ID, category, product ID, quantity, unit price, sales amount, and timestamp.

Finally:
- Write the file to an AWS S3 bucket
"""


import datetime
import pandas as pd
import numpy as np
from s3fs import S3FileSystem

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
    random_days = np.random.randint(0, delta.days)
    
    # Generate a random number of seconds within the current day
    random_seconds = np.random.randint(0, 86399)  # 86399 seconds in a day (0 to 23 hours, 59 minutes, 59 seconds)

    # Create a datetime object for the current date with the random time
    random_datetime = start_date + datetime.timedelta(days=random_days, seconds=random_seconds)

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

def generate_historical_transactions(num_historical_transactions):
    """
    Generates a specified number of historical transactions per day.

    Args:
        num_historical_transactions (int): The number of historical transactions to generate.

    Returns:
        None. The generated transactions are stored in the DataFrame `df`.

    Code Analysis:
        - Initialize an empty list to store the transactions.
        - For each transaction to be generated:
            - Generate a random but unique sales ID between 1000 and 9999.
            - Select a random customer ID from the given list of customer IDs.
            - Select a random product category from the given list of product categories.
            - Select a random product ID within the selected category.
            - Generate a random quantity between 1 and 5 except for products in category 101 and 102.
            - Get the fixed price of the selected product ID.
            - Calculate the sales amount by multiplying the unit price with the quantity.
            - Generate a random timestamp within the specified date range.
            - Create a dictionary with the transaction data.
            - Append the transaction data dictionary to the list of transactions.
        - Create a pandas DataFrame from the list of transactions.
    """
    transactions = []
    for _ in range(num_historical_transactions):
        sales_id = next(sales_id_generator)
        customer_id = np.random.choice(customer_ids)
        category = np.random.choice(product_categoryID)
        product_id = np.random.choice(product_ids[category])

        # Determine the quantity of the product based on product category
        if category == "101":
            quantity = np.random.randint(1, 2)
        elif category == "102":
            quantity = 1
        else:
            quantity = np.random.randint(1, 5)
        unit_price = product_prices.get(product_id, 0)  # Get the fixed price for the product
        price = np.round(unit_price * quantity, decimals=2)
        payment_method = np.random.choice(payment_methods)
        timestamp = generate_random_timestamp()

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

        transactions.append(transaction_data)

    # Create the DataFrame from the list of transactions
    df = pd.DataFrame(transactions)
    return df

# Number of historical transactions to generate 
num_historical_transactions = 500 # target number should be >= 500000

# Generate historical transactions
df =generate_historical_transactions(num_historical_transactions)

# Sort transactions by date and sales ID
historical_transactions = df.sort_values(by=['DateTime', 'Sales ID'], ignore_index=True)

historical_transactions.to_csv('historical_transactions.csv', index=False)

# Number of historical transactions to generate 
num_historical_transactions = 500  # Update as needed

if __name__ == "__main__":
    try:
        # Generate historical transactions and save to CSV
        df = generate_historical_transactions(num_historical_transactions)
        historical_transactions = df.sort_values(by=['DateTime', 'Sales ID'], ignore_index=True)
        historical_transactions.to_csv('historical_transactions.csv', index=False)

        # AWS S3 credentials
        aws_access_key = ' YOUR ACCESS KEY'
        aws_secret_key = ' YOUR SECRET KEY'
        bucket_name = 'bucket name'
        local_file_path = 'historical_transactions.csv'
        s3_file_path = 'historical_transactions.csv'

        # Upload the CSV file to S3
        s3 = S3FileSystem(key=aws_access_key, secret=aws_secret_key)
        with open(local_file_path, 'rb') as local_file:
            with s3.open(f'{bucket_name}/{s3_file_path}', 'wb') as s3_file:
                s3_file.write(local_file.read())
        print(f'{local_file_path} uploaded to s3://{bucket_name}/{s3_file_path}')
    except Exception as e:
        print(f"Error generating historical transactions or uploading to S3: {str(e)}")
