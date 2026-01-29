# import boto3                                         #list all buckets 

# # Example: S3 bucket list
# s3 = boto3.client("s3")
# buckets = s3.list_buckets()
# print([b['Name'] for b in buckets['Buckets']])





import boto3                                            #creatinga s3 bucket
s3 = boto3.client("s3", region_name="ap-south-1")       #creating a client for s3

bucket_name = "shivam-test-bucket-2026"  # unique name  globally

# Bucket create karna
s3.create_bucket(                              #bucket creation method
    Bucket=bucket_name,
    CreateBucketConfiguration={'LocationConstraint': 'ap-south-1'}
)

print(f"Bucket '{bucket_name}' created successfully!")

# Ab check karne ke liye list
buckets = s3.list_buckets()
print("All Buckets:", [b['Name'] for b in buckets['Buckets']])

