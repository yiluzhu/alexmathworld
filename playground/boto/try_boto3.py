import decimal
import boto3


# Get the service resource.
dynamodb = boto3.resource('dynamodb', endpoint_url='http://localhost:8000')


def create_movie_table():
    try:
        table = dynamodb.create_table(
            TableName='Movies',
            KeySchema=[
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'  # Partition key
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'  # Sort key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table
    except dynamodb.meta.client.exceptions.ResourceInUseException:
        print('table already exists')


def get_all_tables():
    return list(dynamodb.tables.all())


def scan_table():
    table = dynamodb.Table('Movies')
    all_items = table.scan()
    return all_items


def put_movie():
    table = dynamodb.Table('Movies')
    response = table.put_item(
       Item={
            'year': decimal.Decimal('2000'),
            'title': 'Movie A',
            'info': {
                'plot': '',
                'rating': decimal.Decimal('5.1')
            }
        }
    )
    return response


if __name__ == '__main__':
    # movie_table = create_movie_table()
    # print("Table status:", movie_table.table_status)
    # print(get_all_tables())
    # print('Total items in table Movies:', scan_table()['Count'])
    resp = put_movie()
    print(resp)
