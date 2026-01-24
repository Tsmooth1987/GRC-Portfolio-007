# AWS Audit Report Generator

This tool automates the collection of AWS security-related information and generates an Excel report for audit purposes.

## Features

- Retrieves IAM user information
- Collects EC2 instance details
- Generates a formatted Excel report with multiple sheets
- Includes timestamped reports for historical tracking

## Prerequisites

- Python 3.7+
- AWS CLI configured with appropriate credentials
- Required Python packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure your AWS credentials are properly configured (usually in `~/.aws/credentials`)
2. Run the script:
   ```bash
   python aws_audit_report.py
   ```
3. The script will generate an Excel file named `aws_audit_report_YYYYMMDD_HHMMSS.xlsx`

## Report Contents

The generated Excel file contains the following sheets:

1. **Summary**: Overview of the audit including timestamp and resource counts
2. **IAM Users**: List of all IAM users in the account
3. **EC2 Instances**: Detailed information about EC2 instances

## Customization

You can extend the script to include additional AWS services by:
1. Adding new functions to collect data from other AWS services
2. Creating new DataFrames for the collected data
3. Adding the DataFrames to the Excel report in the `generate_excel_report` function

## Security Note

- Ensure your AWS credentials have the minimum required permissions
- The generated Excel file may contain sensitive information - handle it securely
- Consider encrypting the output file if it contains sensitive data

## License

This project is for educational purposes. Use at your own risk.
