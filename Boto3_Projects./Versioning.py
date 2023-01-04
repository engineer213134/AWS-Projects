#Create bucket versioning you need to create a bucket versioning class
def enable_bucket_versioning(bucket_name):
    bkt_versioning = s3_resource.BucketVersioning(bucket_name)
    bkt_versioning.enable()
    print(bkt_versioning.status)
    
#Run command in terminal
enable_bucket_versioning(first_bucket_name)

#create two new versions for the first file Object, one with the contents of the original file and one with the contents of the third file
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
   first_file_name)
s3_resource.Object(first_bucket_name, first_file_name).upload_file(
   third_file_name)

#Now reupload the second file, which will create a new version:
s3_resource.Object(first_bucket_name, second_file_name).upload_file(
    second_file_name)

#Retrive version of latest version of the object 
s3_resource.Object(first_bucket_name, first_file_name).version_id
