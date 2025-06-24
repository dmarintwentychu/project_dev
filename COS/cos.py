import ibm_boto3
from ibm_botocore.client import Config
import os

class COS:
    def __init__(self):
        self.bucket_name = "somebucket-for-interview"
        self.file_name = "README.md"
        self.download_path = "./result/README.md"

        self.cos_client = ibm_boto3.client(
            "s3",
            ibm_api_key_id="AerehQeOtiZljYn3cp3Rv5--PTLRVXJvROW8YJib6Fd6",
            ibm_service_instance_id="crn:v1:bluemix:public:cloud-object-storage:global:a/90f4ad63175d479a84ee05b5445012dd:33efa59c-686f-4452-8b32-3a40de8215b3::",
            config=Config(signature_version="oauth"),
            endpoint_url="https://s3.direct.eu-es.cloud-object-storage.appdomain.cloud"
        )


    def download_file(self):
        print("Descargando...")
        response = self.cos_client.get_object(
            Bucket=self.bucket_name,
            Key=self.file_name
        )

        os.makedirs(os.path.dirname(self.download_path), exist_ok=True)

        with open(self.download_path, 'wb') as file:
            file.write(response['Body'].read())




cos = COS()
cos.download_file()
