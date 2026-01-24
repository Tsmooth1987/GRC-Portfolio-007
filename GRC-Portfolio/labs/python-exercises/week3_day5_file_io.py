# --- Week 3: File I/O (Reading from and Writing to a file) ---

# This script now reads server names from one file and writes a report to another.

input_filename = 'servers.txt'
output_filename = 'audit_report.txt'

print(f"--- Reading from '{input_filename}' and writing to '{output_filename}' ---")

try:
    # We can open multiple files at once.
    # 'r' for the input file (read mode)
    # 'w' for the output file (write mode). 'w' will create the file if it doesn't exist,
    # or overwrite it if it does.
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        
        outfile.write("--- Server Audit Report ---\n")
        outfile.write("The following servers were processed:\n")
        outfile.write("----------------------------------\n")

        for line in infile:
            server_name = line.strip()
            print(f"Processing: {server_name}")
            
            # Write the server name to our report file.
            # We add '\n' to create a new line in the output file.
            outfile.write(f"{server_name}\n")

        outfile.write("----------------------------------\n")
        outfile.write("Audit complete.\n")

except FileNotFoundError:
    print(f"Error: The input file '{input_filename}' was not found.")

print(f"--- Report saved to '{output_filename}' ---")
