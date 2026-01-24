# --- Week 4: Professional Logging ---

import boto3
import pandas as pd
import logging # Import the logging library

# --- Step 1: Configure the logging ---

# This is the basic configuration for our logger.
# - level=logging.INFO: We want to see all messages that are 'INFO' level or higher (INFO, WARNING, ERROR).
# - format: This defines how each log message will look. It includes the timestamp, level, and message.
# - handlers: This tells the logger where to send the messages.
#   - logging.FileHandler('audit.log'): Send messages to a file named 'audit.log'.
#   - logging.StreamHandler(): Send messages to the console (your screen).

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('audit.log'),
        logging.StreamHandler()
    ]
)

logging.info("--- Starting IAM User Audit with Logging ---")

# --- Step 2: Use the logger throughout the script ---

iam_client = boto3.client('iam')

try:
    logging.info("Connecting to AWS and requesting IAM user list...")
    response = iam_client.list_users()
    users = response['Users']
    logging.info(f"Found {len(users)} IAM user(s) in the account.")

    if users:
        user_data = []
        for user in users:
            user_info = {
                'UserName': user['UserName'],
                'CreateDate': user['CreateDate'].strftime("%Y-%m-%d"),
                'LastPasswordUse': user.get('PasswordLastUsed', 'N/A')
            }
            user_data.append(user_info)
        
        df = pd.DataFrame(user_data)
        logging.info("Successfully loaded user data into pandas DataFrame.")
        
        # For a log, we can format the DataFrame as a multi-line string
        logging.info(f"IAM User Report:\n{df.to_string()}")
    else:
        logging.info("No IAM users to report on.")

except Exception as e:
    # Use logging.error to record any exceptions that occur.
    logging.error(f"An unexpected error occurred: {e}")

logging.info("--- Audit Complete ---")
