from decimal import Decimal
import json
import time
import boto3


dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


def load_movies(movies):
    table = dynamodb.Table('Movies')
    for movie in movies:
        table.put_item(Item=movie)


if __name__ == '__main__':
    with open("moviedata.json") as json_file:
        movie_list = json.load(json_file, parse_float=Decimal)
    t0 = time.time()
    load_movies(movie_list)
    print(f'Finished. It took {time.time() - t0} seconds.')
