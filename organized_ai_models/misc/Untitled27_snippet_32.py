# Commenting out S3 configuration for now
# aws_access_key = "YOUR_NEW_AWS_ACCESS_KEY"
# aws_secret_key = "YOUR_NEW_AWS_SECRET_KEY"
# try:
#     s3 = boto3.client(
#         "s3",
#         aws_access_key_id=aws_access_key,
#         aws_secret_access_key=aws_secret_key,
#     )
#     # List available buckets to auto-detect configuration
#     response = s3.list_buckets()
#     buckets = [bucket["Name"] for bucket in response["Buckets"]]
#     if buckets:
#         aws_bucket_name = buckets[0]
#         print(f"Detected S3 Bucket: {aws_bucket_name}")
#     else:
#         raise ValueError("No S3 buckets found. Falling back to Firebase.")
# except Exception as e:
#     print(f"Error configuring S3: {e}")
#     aws_bucket_name = None
