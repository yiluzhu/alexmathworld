import os
import boto3


# Get the service resource.
if os.environ.get('ALEX_WORLD_ENV') == 'aws':
    db = boto3.resource('dynamodb', region_name='eu-west-2')
else:
    db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')


def create_comment_table():
    try:
        table = db.create_table(
            TableName='Comments',
            KeySchema=[
                {
                    'AttributeName': 'name',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'timestamp',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'name',
                    'AttributeType': 'S'
                },
                {
                    'AttributeName': 'timestamp',
                    'AttributeType': 'S'
                },
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table
    except db.meta.client.exceptions.ResourceInUseException:
        pass  # table already exists
