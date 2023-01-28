In this project I will be implementing a simple serverless application which uses Web Identity Federation.
The application runs using the following technologies

S3 for front-end application hosting
Google API Project as an ID Provider
Cognito and IAM Roles to swap Google Token for AWS credentials
The application runs from a browser, gets the user to login using a Google ID and then loads all images from a private S3 bucket into a browser using presignedURLs.

This advanced demo consists of 6 stages :-

STAGE 1 : Provision the environment and review tasks
STAGE 2 : Create Google API Project & Client ID
STAGE 3 : Create Cognito Identity Pool
STAGE 4 : Update App Bucket & Test ApplicationThis project will be creating a basic web application and using federation 
