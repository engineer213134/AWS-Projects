#How to change the storage classes of a uploaded object in the S3 bucket

third_object.upload_file(third_file_name, ExtraArgs={'ServerSideEncryption': 'AES256','StorageClass': 'STANDARD_IA'})
