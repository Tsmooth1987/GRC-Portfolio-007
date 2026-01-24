# --- Week 4: Analyzing AWS Data with Boto3 and Pandas ---

import boto3
import pandas as pd  # It's a standard convention to import pandas as 'pd'
from datetime import datetime, timezone

print("--- Starting IAM User Audit with Boto3 and Pandas ---")

# Create a client to connect to the IAM service
iam_client = boto3.client('iam')

# --- Step 1: Get the data from AWS using Boto3 ---
try:
    # Get a list of all IAM users
    response = iam_client.list_users()
    users = response['Users']
    print(f"Found {len(users)} IAM user(s) in the account.")

    # --- Step 2: Load the data into a Pandas DataFrame ---
    
    # We create a list of dictionaries, which is a perfect format for pandas
    user_data = []
    for user in users:
        user_info = {
            'UserName': user['UserName'],
            'CreateDate': user['CreateDate'].strftime("%Y-%m-%d"), # Format the date
            'LastPasswordUse': user.get('PasswordLastUsed', 'N/A') # Use .get() for optional keys
        }
        user_data.append(user_info)

    # Create the DataFrame from our list of user data
    df = pd.DataFrame(user_data)

    # --- Step 3: Analyze and display the data with Pandas ---

    print("\n--- IAM User Report ---")
    if not df.empty:
        # Pandas DataFrames have a beautiful string representation, perfect for printing.
        print(df.to_string())
    else:
        print("No user data to display.")

except Exception as e:
    print(f"An error occurred: {e}")

print("\n--- Audit Complete ---")
