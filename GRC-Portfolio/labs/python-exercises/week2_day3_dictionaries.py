# --- Week 2: Dictionaries ---

# A dictionary stores data in key-value pairs. It's perfect for holding
# different pieces of information about a single object.
# Dictionaries are enclosed in curly braces {}.

finding = {
    "id": "finding-002",
    "description": "The S3 bucket 'tjsbucketforhisbuckets' does not have access logging enabled.",
    "risk_level": "Medium",
    "status": "Open",
    "days_open": 12
}

# --- Accessing Data in a Dictionary ---

# You access a value by using its key inside square brackets [].

print("--- Analyzing Compliance Finding ---")
print(f"ID: {finding['id']}")
print(f"Description: {finding['description']}")
print(f"Risk Level: {finding['risk_level']}")

# You can use this data in your logic, just like with any other variable.
if finding['risk_level'] == "Medium" and finding['days_open'] > 10:
    print("\nAlert: This medium-risk finding is overdue for remediation!")

print("--- Analysis Complete ---")
