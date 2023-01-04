#Create a new file and upload to S3 bucket usiing server side encryption
#Create file
third_file_name = create_temp_file(300, 'thirdfile.txt', 't')
third_object = s3_resource.Object(first_bucket_name, third_file_name)
#Upload object to S3 bucket
third_object.upload_file(third_file_name, ExtraArgs={
                         'ServerSideEncryption': 'AES256'})

#Confirm algorithm used on object uploaded
third_object.server_side_encryption
