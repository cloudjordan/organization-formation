# organization-formation
Manage AWS Organizations, create Organization Units, and provision accounts securely. 

This project demonstrates the use of AWS OrgFormation and Python to manage AWS Organizations.

## Project Overview

The project showcases the following:

- **AWS OrgFormation**: A third-party tool available on GitHub that enables Infrastructure as Code for AWS Organizations allowing automation of account creation and resource provisioning. 

In my example, I have a main admin account, production account and development account. The production and development accounts exist in their own organizational units within AWS Organizations.

- **Python**: A Python script (`secret_manager.py`) that interacts with AWS Secrets Manager to protect sensitive data, such as account credentials in the `organization.yml` file. When the script is executed, it retrieves data from Secrets Manager and updates the YAML file. 

## Project Setup

To run the project, follow these steps:

1. Install AWS CLI and configure it with your AWS credentials.

2. Install AWS OrgFormation CLI following the instructions provided in the official GitHub repository.

3. Install Python 3.x and the required dependencies (Boto3, YAML libraries).

4. Set up AWS Secrets Manager and store the sensitive data, such as email addresses, as key-value pairs.

5. Update the `secret_manager.py` script with the necessary keys from AWS Secrets Manager. Replace the placeholders in the script with the actual keys to retrieve the sensitive data.

6. Update the `organization.yml` file with your desired organization structure and placeholders for sensitive data.

7. Run the Python script (`secret_manager.py`) to update the `organization.yml` file with the actual values from Secrets Manager.



