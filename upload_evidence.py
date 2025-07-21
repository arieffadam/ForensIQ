import boto3

def upload_file(bucket, key, local_path):
    s3 = boto3.client('s3')
    s3.upload_file(local_path, bucket, key)
    print(f"Uploaded {local_path} to s3://{bucket}/{key}")

if __name__ == "__main__":
    # Replace with your bucket, key, and file path
    upload_file("my-evidence-bucket", "sample-case/sample-file.txt", "sample-file.txt")