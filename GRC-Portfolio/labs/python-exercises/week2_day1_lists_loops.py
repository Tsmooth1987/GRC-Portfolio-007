# --- Week 2: Lists and For Loops ---

# A list is a way to store multiple items in a single variable.
# The items are inside square brackets [], separated by commas.
unpatched_servers = [
    "server-db-01",
    "server-web-03",
    "server-app-02",
    "server-cache-01"
]

print("--- Starting Server Patch Audit ---")

# A 'for' loop lets us run the same block of code for each item in a list.
# The syntax is: for item_variable in list_variable:
# 'server' is a temporary variable that will hold one item from the list at a time.

for server in unpatched_servers:
    # This indented block of code will run once for every server in the list.
    # Notice how we use the 'server' variable to print the name of the current server.
    print(f"Action Required: The server '{server}' is unpatched and needs immediate attention.")

print("--- Audit Complete ---")
