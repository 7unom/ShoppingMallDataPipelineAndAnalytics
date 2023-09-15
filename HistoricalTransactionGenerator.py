"""
Generates historical transactions by randomly selecting customer IDs, product categories, product IDs, quantities, and timestamps. Calculates the total amount for each transaction based on the fixed prices of the products. Stores the transactions in a pandas DataFrame and sorts them by timestamp and sales ID.

Inputs:
- product_categories: A list of product categories.
- product_ids: A dictionary mapping each product category to a list of product IDs within that category.
- customer_ids: A list of customer IDs.
- product_prices: A dictionary mapping each product ID to its fixed price.
- num_transactions_per_day: The number of historical transactions to generate per day.

Outputs:
- Sorted DataFrame containing the historical transactions, with columns for sales ID, customer ID, category, product ID, quantity, unit price, sales amount, and timestamp.
"""


import random
import datetime
import pandas as pd

# Sample product categories
product_categories = ["Electronics", "Clothing", "Books", "Health & Personal Care"]

# Sample product IDs within each category
product_ids = {
    "Electronics": ["E1", "E2", "E3", "E4"],
    "Clothing": ["C1", "C2", "C3", "C4"],
    "Books": ["B1", "B2", "B3", "B4"],
    "Health & Personal Care": ["H1", "H2", "H3", "H4"]
}

# Sample customer IDs
customer_ids = [1001, 1002, 1003, 1004, 1005]

# Define fixed prices for each product ID
product_prices = {
    "E1": 199.99,
    "E2": 149.99,
    "E3": 99.99,
    "E4": 79.99,
    "C1": 49.99,
    "C2": 39.99,
    "C3": 29.99,
    "C4": 19.99,
    "B1": 12.99,
    "B2": 14.99,
    "B3": 9.99,
    "B4": 11.99,
    "H1": 149.99,
    "H2": 99.99,
    "H3": 69.99,
    "H4": 119.99,
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



# Initialize an empty DataFrame
columns = ["Sales ID", "Customer ID", "Category", "Product ID", "Quantity", "Unit Price", "Sales Amount", "Timestamp"]
df = pd.DataFrame(columns=columns)

def generate_historical_transactions(num_transactions_per_day):
    transactions = []
    for _ in range(num_transactions_per_day):
        sales_id = random.randint(1000, 9999)
        customer_id = random.choice(customer_ids)
        category = random.choice(product_categories)
        product_id = random.choice(product_ids[category])
        quantity = random.randint(1, 5)
        unit_price = product_prices.get(product_id, 0)  # Get the fixed price for the product
        sales_amount = unit_price * quantity
        timestamp = generate_random_timestamp()

        # Create a dictionary for the current transaction
        transaction_data = {
            "Sales ID": sales_id,
            "Customer ID": customer_id,
            "Category": category,
            "Product ID": product_id,
            "Quantity": quantity,
            "Unit Price": unit_price,
            "Sales Amount": sales_amount,
            "Timestamp": timestamp
        }

        transactions.append(transaction_data)

    global df  # Use the global DataFrame
    df = pd.DataFrame(transactions)

# Number of historical transactions to generate 
num_historical_transactions = 500

# Generate historical transactions
generate_historical_transactions(num_historical_transactions)

# Print the DataFrame with all transactions
df_sorted = df.sort_values(by=['Timestamp', 'Sales ID'], ignore_index=True)
print(df_sorted.head())