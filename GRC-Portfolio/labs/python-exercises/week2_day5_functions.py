# --- Week 2: Functions ---

# A function is a reusable block of code that performs a specific action.
# We define a function using the 'def' keyword, followed by a name and parentheses ().
# This function takes one piece of information (a 'finding_dict') as input.

def process_finding(finding_dict):
    """Takes a finding dictionary and prints a formatted summary."""
    print(f"--- Processing Finding ID: {finding_dict['id']} ---")
    print(f"Description: {finding_dict['description']}")
    
    # We can still use logic inside a function.
    if finding_dict['risk_level'] == "High":
        print(f"Risk Level: {finding_dict['risk_level']} -> ACTION REQUIRED IMMEDIATELY")
    else:
        print(f"Risk Level: {finding_dict['risk_level']}")
    print("--------------------------------------------------\n")

# --- Main part of our script ---

# Here is our data: a LIST of DICTIONARIES.
# This is a very common structure you will work with.
all_findings = [
    {
        "id": "finding-003",
        "description": "EC2 instance 'i-12345' has port 22 open to the world.",
        "risk_level": "High"
    },
    {
        "id": "finding-004",
        "description": "IAM user 'dev-user' has not enabled Multi-Factor Authentication (MFA).",
        "risk_level": "Medium"
    },
    {
        "id": "finding-005",
        "description": "CloudTrail logging is not enabled in the 'ap-southeast-2' region.",
        "risk_level": "High"
    }
]

# Now, we loop through our list of findings.
for current_finding in all_findings:
    # For each finding, we 'call' our function, passing the current finding into it.
    process_finding(current_finding)

print("All findings processed.")
