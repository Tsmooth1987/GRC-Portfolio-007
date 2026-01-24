# --- Week 4: Real-World AWS Automation with Boto3 ---

# We import the boto3 library, which allows Python to talk to AWS.
import boto3

print("--- Attempting to list S3 buckets from your AWS account ---")

# We create a 'client' for the S3 service. This is our connection to S3.
# Boto3 will automatically find the credentials you configured for the AWS CLI.
s3_client = boto3.client('s3')

# We call the 'list_buckets' function on our client.
# This sends a request to AWS to get a list of all your S3 buckets.
try:
    response = s3_client.list_buckets()

    print("Successfully connected to AWS. Buckets found:")
    
    # The actual list of buckets is inside the 'Buckets' key in the response.
    # We loop through this list to print the name of each bucket.
    for bucket in response['Buckets']:
        # Each 'bucket' is a dictionary. The name is in the 'Name' key.
        print(f"  - {bucket['Name']}")

except Exception as e:
    print(f"An error occurred while connecting to AWS: {e}")
    print("Please ensure your AWS CLI is configured correctly with valid credentials.")

print("--- Script finished ---")
