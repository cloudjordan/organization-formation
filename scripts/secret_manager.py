import json
import boto3
import yaml
from botocore.exceptions import ClientError


def get_secret_and_update_yaml():
    secret_name = "organizationEmails"
    region_name = "eu-central-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    # Converting the JSON string to a Python dictionary
    secret = json.loads(get_secret_value_response['SecretString'])

    # Load the organization.yml file as a dictionary
    with open('../organization.yml', 'r') as f:
        yaml_data = yaml.safe_load(f)

    # Update the sensitive data in the yaml_data using the secret key/value pairs
    yaml_data['Organization']['ManagementAccount']['Properties']['RootEmail'] = secret["master_email"]
    yaml_data['Organization']['ManagementAccount']['Properties']["AccountId"] = secret["account_id"]
    yaml_data['Organization']['ManagementAccount']['Properties']["AccountName"] = secret["account_name"]
    yaml_data['Organization']['DevelopmentOU']['Properties']['Accounts']['Properties']['RootEmail'] = secret["dev_email"]
    yaml_data['Organization']['ProductionOU']['Properties']['Accounts']['Properties']['RootEmail'] = secret["prod_email"]

    # Write the modified data back to the YAML file
    with open('../organization.yml', 'w') as f:
        yaml.dump(yaml_data, f, sort_keys=True, indent=2)


# Execute the function
get_secret_and_update_yaml()
