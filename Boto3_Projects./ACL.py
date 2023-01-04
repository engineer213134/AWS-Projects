#Using BOTO3 to issue ACL on new objects in a S3 bucket

#Issue commands to create a temp file and place in S3 
second_file_name = create_temp_file(400, 'secondfile.txt', 's')
second_object = s3_resource.Object(first_bucket.name, second_file_name)
#Set permissions of object as public by using a ACL
second_object.upload_file(second_file_name, ExtraArgs={
                          'ACL': 'public-read'})


#Getting ObjectAcl instance from the object and assighning it second_object_acl
second_object_acl = second_object.Acl()

#See who has access to object use grant attribute
second_object_acl.grants

#To make object private again with out needing to upload
response = second_object_acl.put(ACL='private')
