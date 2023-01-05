#How get info or apply an opertaion to all S3 resources

#Bucket tranversal, gives list of all bucket instances
for bucket in s3_resource.buckets.all():
  print(bucket.name)
  
#Object transversal 

  
