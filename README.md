# AWS Lambda S3 Log Cleaner (using Lambda, Boto3 & AWS Event Bridge)

### Flowchart-style diagram
<img width="468" height="643" alt="image" src="https://github.com/user-attachments/assets/fe459820-3955-48dd-a4ab-a9d82d59aae7" />

## Project Overview
This project demonstrates how to use **AWS Lambda** with **Amazon EventBridge Scheduler** to automatically clean up old log files from an S3 bucket. The Lambda function checks object timestamps and deletes files older than a configurable retention period.

---

## Key Features
- **Configurable retention** via environment variable (`RETENTION_DAYS`).
- **Automated cleanup** of S3 objects older than cutoff date.
- **IAM role with least privilege** for secure access.
- **Scheduled execution** using EventBridge cron expressions.

---

## Implementation Steps
1. **S3 Bucket**  
   - Created bucket: `sweta-log-cleaner-bucket`.
<img width="940" height="343" alt="image" src="https://github.com/user-attachments/assets/673d642b-c413-4758-b4ba-166bbffb1d2e" />

2. **Lambda Function**  
   - Runtime: Python 3.14  
   - Code deletes objects older than `RETENTION_DAYS`.
<img width="940" height="440" alt="image" src="https://github.com/user-attachments/assets/d70bf31e-3df4-47b7-9ea1-97794e7b88c9" />
<img width="940" height="289" alt="image" src="https://github.com/user-attachments/assets/cc91a7f2-bfba-42b0-9788-50701870c95b" />

3. **Environment Variables**  
   - `BUCKET_NAME = sweta-log-cleaner-bucket`  
   - `RETENTION_DAYS = 90` (initial setup)  
   - **Changed to `0` for testing**, since no logs older than 90 days existed.
<img width="940" height="274" alt="image" src="https://github.com/user-attachments/assets/7f952ba0-0aea-4ae5-82e9-6a59129b446d" />

4. **IAM Role Permissions**  
   - Attached `AWSLambdaBasicExecutionRole` (CloudWatch logging).  
   - Added inline policy for S3 access:
     - `s3:ListBucket` → bucket level.  
     - `s3:GetObject`, `s3:DeleteObject` → object level.
<img width="940" height="455" alt="image" src="https://github.com/user-attachments/assets/5195e92a-9fb2-4377-91cc-f4bc56de7bb7" />
<img width="940" height="81" alt="image" src="https://github.com/user-attachments/assets/d710fa5d-de15-4c36-a24b-cc47e9e75cce" />


5. **EventBridge Scheduler**  
   - Initial cron: `cron(0 0 ? * SUN *)` → every Sunday at midnight UTC.  
   - **Changed to `cron(0/5 * ? * * *)` → every 5 minutes** for testing.
<img width="940" height="470" alt="image" src="https://github.com/user-attachments/assets/bf244143-9f8e-4248-9a59-67ea0614f0fe" />
<img width="940" height="574" alt="image" src="https://github.com/user-attachments/assets/3bcd5aac-51b8-4c69-a780-6b1f640d502f" />

---

## Testing Notes
- With `RETENTION_DAYS=90`: No deletions occurred (no files older than 90 days).  
- With `RETENTION_DAYS=0`: All files were immediately deleted.  
- CloudWatch logs confirmed deletion messages:
<img width="940" height="444" alt="image" src="https://github.com/user-attachments/assets/a7c692b5-4fa6-4d53-8906-fe53aa88095b" />

# Deleting test.log, last modified 2026-03-17
<img width="940" height="316" alt="image" src="https://github.com/user-attachments/assets/5eb0c724-a01b-41c2-9702-03313ab05c36" />

## Validation
- Lambda executed successfully with correct IAM permissions.  
- EventBridge Scheduler triggered Lambda every 5 minutes.  
- S3 bucket verified: files deleted as expected.
<img width="1624" height="800" alt="image" src="https://github.com/user-attachments/assets/c86624f8-e315-4396-aa9f-73e909453673" />

---

# Conclusion
This assignment demonstrates:
- Secure IAM role setup.  
- Lambda function for automated S3 cleanup.  
- EventBridge Scheduler integration.  
- Practical testing adjustments (retention set to 0 days, cron set to 5 minutes) to validate functionality in absence of 90‑day old logs.

<img width="1024" height="1024" alt="image" src="https://github.com/user-attachments/assets/3caaa8e5-42cd-4e9d-95a6-d77a4bbc8c01" />
