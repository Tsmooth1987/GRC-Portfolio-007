# --- Week 2 Exercise: Server Patch Audit ---

# Here is your data: a list of dictionaries.
# Each dictionary represents a server with its name and patch status.
server_list = [
    {
        "name": "server-db-01",
        "is_patched": True
    },
    {
        "name": "server-web-03",
        "is_patched": False
    },
    {
        "name": "server-app-02",
        "is_patched": False
    },
    {
        "name": "server-cache-01",
        "is_patched": True
    },
    {
        "name": "server-loadbalancer-01",
        "is_patched": False
    }
]

print("--- Starting Server Audit ---")
print("The following servers are unpatched:")

# Your task:
# 1. Write a 'for' loop to go through each server in the 'server_list'.
# 2. Inside the loop, write an 'if' statement to check if the
#    server's 'is_patched' value is False.
# 3. If it is False, print the server's 'name'.

# --- WRITE YOUR FOR LOOP AND IF STATEMENT BELOW ---
for server in server_list:
    if not server["is_patched"]:
        print(server["name"])
# ---------------------------------------------------

print("--- Audit Complete ---")
