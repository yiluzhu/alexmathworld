import boto3


def get_db():
    # Run dynamodb locally in cmd:
    #   cd D:\apps\dynamodb_local_latest
    #   java -Djava.library.path=./DynamoDBLocal_lib -jar DynamoDBLocal.jar -sharedDb
    # db = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')
    db = boto3.resource('dynamodb', region_name='eu-west-2')
    return db


def get_comment_table():
    db = get_db()
    table = db.Table('Comments')
    return table


def create_comment_table():
    db = get_db()
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
