import boto3
import json

iam = boto3.client('iam', region_name='us-east-1')
response = iam.list_policies(Scope='Local')
policies = response['Policies']

with open('iam_audit_report.txt', 'w') as report:
    for policy in policies:
        policy_name = policy['PolicyName']
        policy_version = iam.get_policy_version(PolicyArn=policy['Arn'], VersionId=policy['DefaultVersionId'])
        policy_doc = policy_version['PolicyVersion']['Document']
        for statement in policy_doc['Statement']:
            if statement['Effect'] == 'Allow' and statement.get('Resource') == '*':
                warning = f"WARNING: Policy '{policy_name}' has unrestricted resource access!\n"
                print(warning)
                report.write(warning)

    users = iam.list_users()['Users']
    for user in users:
        mfa_devices = iam.list_mfa_devices(UserName=user['UserName'])['MFADevices']
        if not mfa_devices:
            warning = f"WARNING: User '{user['UserName']}' has no MFA enabled!\n"
            print(warning)
            report.write(warning)