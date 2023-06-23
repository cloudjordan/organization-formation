# organization-formation
Manage AWS Organizations, create Organization Units, and provision accounts securely. 

This project demonstrates the use of AWS OrgFormation and Python to manage AWS Organizations. It was intended as my personal project. But others can use it or parts of it for their own project if they want to. 

## Project Overview

The project showcases the following:

- **AWS OrgFormation**: A third-party tool available on GitHub that enables Infrastructure as Code for AWS Organizations allowing automation of account creation and resource provisioning. For more details, check the official github repository for org-formation. 

In my example, I have a main admin account, production account and development account. The production and development accounts exist in their own organizational units within AWS Organizations.

- **Python**: A Python script (`secret_manager.py`) that interacts with AWS Secrets Manager to protect sensitive data, such as account credentials in the `organization.yml` file. When the script is executed, it retrieves data from Secrets Manager and updates the YAML file. 

## Project Setup

Here are some general guidelines for the project:

1. Install AWS CLI and configure it with your AWS credentials.

2. Install AWS OrgFormation CLI following the instructions provided in the official GitHub repository.

3. Install Python 3.x and the required dependencies (Boto3, YAML libraries).

4. Set up AWS Secrets Manager and store the sensitive data, such as email addresses, as key-value pairs.

5. Update the `secret_manager.py` script with the necessary keys from AWS Secrets Manager. Replace the placeholders in the script with the actual keys to retrieve the sensitive data.

6. Update the `organization.yml` file with your desired organization structure and placeholders for sensitive data. Some other properties you may want to consider updating are Alias, AccountName and OrganizationalUnitName.

7. Run the Python script (`secret_manager.py`) to update the `organization.yml` file with the actual values from Secrets Manager.
   
8. To execute the YAML file in AWS, you need to run this command. More details can be found in the official org-formation github repo: `sudo org-formation init organization.yml  --region (specified aws region) --profile (your profile name)` 



