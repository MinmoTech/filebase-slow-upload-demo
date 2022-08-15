import time

import io
import os
from minio import Minio

filebase_api_key = os.environ["FILEBASE_API_KEY"]
filebase_api_secret = os.environ["FILEBASE_API_SECRET"]
filebase_bucket = os.environ["FILEBASE_BUCKET"]
minio_client = Minio(
    "s3.filebase.com",
    access_key=filebase_api_key,
    secret_key=filebase_api_secret,
    secure=True,
    region="us-east-1",
)
for i in range(500):
    # generate random data of size 200kb
    data = bytearray(os.urandom(200 * 1024))
    with io.BytesIO(data) as f:
        # time the upload
        start = time.time()
        minio_client.put_object(
            bucket_name=filebase_bucket,
            object_name=str(i),
            data=f,
            length=len(data),
        )
    end = time.time()
    print(f"{i} uploaded in {end - start} seconds")
