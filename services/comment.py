import logging
import datetime
from db.dynamodb import create_comment_table, db


logger = logging.getLogger(__name__)


class Comment:
    def __init__(self):
        create_comment_table()
        self.table = db.Table('Comments')

    def save_a_comment(self, name, content):
        item = {
            'name': name,
            'timestamp': str(datetime.datetime.now()).rsplit('.', 1)[0],
            'info': {
                'ip': '',
            },
            'content': content,
        }
        response = self.table.put_item(Item=item)
        return response['ResponseMetadata']['HTTPStatusCode']

    def load_all_comments(self):
        response = self.table.scan()
        items = response['Items']
        logger.info(f'Total comments count: {len(items)}')
        return sorted(items, key=lambda x: x['timestamp'], reverse=True)

    def delete_all_comments(self):
        self.table.delete()


if __name__ == '__main__':
    co = Comment()
    # all = co.load_all_comments()
    # print(all)
    # co.delete_all_comments()