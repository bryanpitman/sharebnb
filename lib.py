import json
import boto3
from botocore.client import Config


class AwsBucketApi:

    def __init__(self, bucket_name = None):
        settings = self.get_settings()
        self.bucket_name = bucket_name or settings.get("bucket_name")
        self.bucket  = boto3.client("s3",
            aws_access_key_id = settings.get("user_access_id"),
            aws_secret_access_key = settings.get("user_secret"),
            region_name = settings.get("bucket_region"),
            config = Config(signature_version='s3v4', s3 = {"addressing_style" : "path"})
        )

    def get_settings(self):
        with open("settings.json") as f:
            return json.load(f)

    def generate_presigned_url(self, filename, expires = 3600):
        return self.bucket.generate_presigned_url(
            ClientMethod = "get_object",
            ExpiresIn = expires,
            Params = {
                "Bucket" : self.bucket_name,
                "Key" : filename
            }
        )