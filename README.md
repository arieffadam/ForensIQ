# ForensIQ MVP

A deployment-ready MVP cyber forensics platform on AWS. Analyze evidence files using YARA rules, store case metadata in DynamoDB, and manage files in S3.

## Features

- Upload evidence files to AWS S3
- Automated analysis with YARA rules via AWS Lambda
- Case metadata storage in DynamoDB
- Simple React dashboard for uploads and status

## Prerequisites

- AWS CLI
- Node.js & npm
- Python 3.x
- AWS account with permissions to deploy CloudFormation, Lambda, S3, DynamoDB
- YARA compiled for AWS Lambda (see [AWS Lambda Layers](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html))

## Deployment

### 1. Deploy Core Infrastructure

```sh
aws cloudformation deploy \
  --template-file forensiq-core.yaml \
  --stack-name forensiq-core \
  --parameter-overrides BucketName=my-evidence-bucket TableName=my-case-table
```

### 2. Package & Deploy Lambda Function

- Install dependencies (`requirements.txt`):

  ```
  pip install boto3 yara-python -t ./package
  cp index.py ./package/
  zip -r lambda.zip ./package
  ```

- Add `rules.yar` to a Lambda layer or to `/opt` in your deployment package.

- Create Lambda function and set the environment variable `DYNAMODB_TABLE` to your DynamoDB table name.

- Attach IAM role for S3 and DynamoDB access.

### 3. Run the Frontend

```sh
cd frontend
npm install
npm start
```

Update `frontend/.env` with your API endpoint if needed.

### 4. Upload Evidence Example

See `upload_evidence.py` for a sample script to upload files to S3.

### 5. Usage

- Upload evidence via the dashboard or script
- Lambda analyzes the file and updates DynamoDB
- Dashboard displays status and results

## Folder Structure

```
/
|-- index.py
|-- index.js
|-- forensiq-core.yaml
|-- rules.yar
|-- README.md
|-- upload_evidence.py
|-- frontend/
    |-- index.js
    |-- ...
```

## AWS Resources

- S3 Bucket: stores evidence files
- DynamoDB Table: stores case metadata and YARA results
- Lambda Function: performs analysis
- IAM Roles: secure access

## Notes

- Update `rules.yar` with more signatures as needed
- Ensure Lambda layer includes YARA
- Secure your AWS resources with least privilege policies
