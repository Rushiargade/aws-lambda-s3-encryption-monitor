import boto3
from botocore.exceptions import ClientError

def lambda_handler(event, context):
    s3 = boto3.client('s3')

    response = s3.list_buckets()
    buckets = response.get('Buckets', [])

    unencrypted_buckets = []

    for bucket in buckets:
        bucket_name = bucket['Name']

        try:
            s3.get_bucket_encryption(Bucket=bucket_name)
            print(f"Bucket '{bucket_name}' has encryption enabled")

        except ClientError as e:
            error_code = e.response['Error']['Code']

            # No encryption configured
            if error_code == 'ServerSideEncryptionConfigurationNotFoundError':
                print(f"Bucket '{bucket_name}' does NOT have encryption enabled")
                unencrypted_buckets.append(bucket_name)

            # Access denied or other issue
            else:
                print(f"Skipping bucket '{bucket_name}' due to error: {error_code}")

        # 🚨 Safety break to avoid timeout (for assignment)
        if context.get_remaining_time_in_millis() < 3000:
            print("Stopping execution to avoid timeout")
            break

    print("==== SUMMARY ====")
    if unencrypted_buckets:
        print("Unencrypted buckets found:")
        for b in unencrypted_buckets:
            print(b)
    else:
        print("All checked buckets have encryption enabled")

    return {
        "statusCode": 200,
        "body": "S3 encryption compliance check completed"
    }
