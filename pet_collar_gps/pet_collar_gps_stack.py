import os

from aws_cdk import (
    aws_dynamodb as dynamodb,
    aws_lambda as lambda_,
    aws_apigateway as apigateway,
    core
)
 
class PetCollarGpsStack(core.Stack):

    def __init__(self, scope: core.Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Create a DynamoDB table to store the GPS locations.
        table = dynamodb.Table(self, "PetGpsLocations",
            partition_key=dynamodb.Attribute(name="PetId", type=dynamodb.AttributeType.STRING),
            sort_key=dynamodb.Attribute(name="Timestamp", type=dynamodb.AttributeType.NUMBER),
            table_name="PetGpsLocations"
        )

        # Create a Lambda function that will read data from the API and populate the DynamoDB table.
        lambda_function = lambda_.Function(self, "GpsProcessor",
            code=lambda_.Code.from_asset(os.path.join(os.getcwd(), "resources")),
            handler="process-gps-datum.main",
            runtime=lambda_.Runtime.PYTHON_3_7
        )
        
        # Grant the function read/write access to the table.
        table.grant_read_write_data(lambda_function)
        
        # Create an API Gateway to act as a proxy for the Lambda.
        apigateway.LambdaRestApi(self, "pet-location-api", handler=lambda_function)