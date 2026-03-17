import boto3
import os
from datetime import datetime, timezone, timedelta

# Initialize S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Use BUCKET_NAME environment variable
    bucket_name = os.environ['BUCKET_NAME']
    
    # Default retention is 90 days if not set
    retention_days = int(os.environ.get('RETENTION_DAYS', '90'))

    # Calculate cutoff date
    cutoff_date = datetime.now(timezone.utc) - timedelta(days=retention_days)

    # List objects in the bucket
    response = s3.list_objects_v2(Bucket=bucket_name)

    if 'Contents' in response:
        for obj in response['Contents']:
            key = obj['Key']
            last_modified = obj['LastModified']

            # Delete if older than cutoff
            if last_modified < cutoff_date:
                print(f"Deleting {key}, last modified {last_modified}")
                s3.delete_object(Bucket=bucket_name, Key=key)

    return {"status": "completed"}

