# AWS IAM Policy Auditor 
A Python script using Boto3 to audit AWS IAM for security risks.

## Setup
1. Clone: `git clone https://github.com/YGcloudsec/aws-iam-auditor.git`
2. Navigate: `cd aws-iam-auditor`
3. Create virtual env: `python -m venv venv`
4. Activate: `venv\Scripts\activate`
5. Install: `pip install boto3 awscli`
6. Configure AWS: `aws configure` (add your credentials)
7. Run: `python iam_auditor.py`

## Features
- Detects overly permissive policies (e.g., `Resource: "*"`).
- Flags users without MFA.