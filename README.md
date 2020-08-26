# Serverless Application Demo using the AWS CDK

This project demonstrates the deployment a serverless application leveraging AWS Lambda for compute, Amazon DynamoDB as a key-value store, and Amazon API Gateway to expose a secure endpoint.
This project also uses the [AWS CDK](https://github.com/aws/aws-cdk) to provision the infrastructure and deploy the application.

This project simulates streaming location data from a GPS enabled device in the [NEMA format](https://en.wikipedia.org/wiki/NMEA_0183) to an API endpoint. AWS Lambda translates the location data from NEMA to latitude/longitude and posts it into a DynamoDB table.
