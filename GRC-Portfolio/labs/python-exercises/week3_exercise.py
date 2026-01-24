# --- Week 3 Exercise: File-Based Server Audit ---

# Your goal is to read server data from a CSV file, identify the unpatched
# servers, and write a report containing only the names of those servers.

input_file = 'servers_with_status.csv'
output_file = 'unpatched_servers_report.txt'

print(f"Starting audit. Reading from '{input_file}'...")

# We will store the names of unpatched servers in this list.
unpatched_servers = []

# --- Your Task, Part 1: Reading and Processing the Input File ---
# 1. Open the 'input_file' for reading.
# 2. Loop through each line in the file.
# 3. For each line, use the .strip() method to remove extra whitespace.
# 4. Use the .split(',') method on the line to get a list containing the
#    server name and its patch status (e.g., ['server-db-01', 'True']).
# 5. Check if the patch status (the second item in the list) is the string 'False'.
# 6. If it is, add the server name (the first item in the list) to the
#    'unpatched_servers' list.

# --- WRITE YOUR CODE FOR PART 1 BELOW ---
try:
    with open(input_file, 'r') as file:
        for line in file:
            # .strip() removes whitespace, .split(',') breaks the line into a list
            parts = line.strip().split(',')
            # Safety check to ensure the line has two parts
            if len(parts) == 2:
                server_name = parts[0]
                patch_status = parts[1]
                # Check if the status is the string 'False'
                if patch_status == 'False':
                    unpatched_servers.append(server_name)
except FileNotFoundError:
    print(f"Error: Input file '{input_file}' not found.")
# ------------------------------------------


# --- Your Task, Part 2: Writing the Output File ---
# 1. Open the 'output_file' for writing.
# 2. Write a header line, like "Unpatched Servers Report:".
# 3. Loop through the 'unpatched_servers' list you created in Part 1.
# 4. For each server name, write it to the output file on a new line.

# --- WRITE YOUR CODE FOR PART 2 BELOW ---
with open(output_file, 'w') as file:
    file.write("Unpatched Servers Report:\n")
    file.write("-------------------------\n")
    for server in unpatched_servers:
        # Add a newline character '\n' to ensure each server is on a new line
        file.write(f"{server}\n")
# ------------------------------------------

print(f"Audit complete. Report saved to '{output_file}'.")
