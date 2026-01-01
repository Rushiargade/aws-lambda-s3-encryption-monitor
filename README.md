# Monitor Unencrypted S3 Buckets Using AWS Lambda and Boto3

## 📌 Objective
The objective of this project is to enhance AWS security by identifying Amazon S3 buckets that do not have server-side encryption enabled. This is achieved using AWS Lambda and the Boto3 Python SDK.

---

## 🛠 AWS Services Used
- Amazon S3
- AWS Lambda
- AWS IAM
- Amazon CloudWatch Logs
- Boto3 (AWS SDK for Python)

---

## 🔐 Security Use Case
Server-side encryption protects data at rest in S3. This Lambda function helps identify buckets that are not compliant with encryption best practices.

---

## 🧾 IAM Role & Permissions
The Lambda function uses an IAM role with the following policies:
- `AmazonS3ReadOnlyAccess`
- `AWSLambdaBasicExecutionRole`

These permissions allow the function to list buckets, check encryption status, and write logs.

---

## 🧠 Lambda Function Workflow
1. Initialize the Amazon S3 client using Boto3
2. Retrieve a list of all S3 buckets
3. Check each bucket for server-side encryption
4. Identify buckets without encryption enabled
5. Log unencrypted bucket names to CloudWatch Logs

---

## 🧪 Testing Procedure
1. Create multiple S3 buckets
2. Enable server-side encryption on some buckets
3. Leave encryption disabled on at least one bucket
4. Manually invoke the Lambda function
5. Review CloudWatch logs to identify unencrypted buckets

---

## 📊 Logging & Monitoring
- Lambda execution logs are stored in Amazon CloudWatch
- Logs clearly indicate:
  - Buckets with encryption enabled
  - Buckets without encryption enabled

---

## ✅ Result
After execution, the Lambda function successfully detects and logs all S3 buckets that do not have server-side encryption enabled.

---
