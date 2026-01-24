# --- Variables and Data Types ---

# A variable is like a labeled box for storing information.
# Here, we create a variable named 'finding_id' and store the text "finding-001" in it.

# 1. String (str): Used for text. Must be in quotes.
finding_id = "finding-001"
finding_description = "User 'test-user' has not rotated access keys in 92 days."

# 2. Integer (int): Used for whole numbers.
risk_score = 85
days_overdue = 2

# 3. Boolean (bool): Used for True or False status.
is_high_risk = True
remediation_required = True

# --- Using the variables ---

# The print() function displays the value stored in a variable.
print("--- GRC Finding Details ---")

# We can print the variables directly.
print("Finding ID:", finding_id)
print("Description:", finding_description)
print("Risk Score:", risk_score)
print("Is High Risk?", is_high_risk)

# You can also combine them to create more meaningful output.
print("\nThis finding is", days_overdue, "days overdue and requires remediation:", remediation_required)
print("---------------------------")
