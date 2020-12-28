import logging
import datetime
from chalicelib.db.dynamodb import create_comment_table, get_comment_table


logger = logging.getLogger(__name__)


class Comment:
    def __init__(self):
        create_comment_table()
        self.table = get_comment_table()

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

    def delete_one_comment(self, name, timestamp):
        self.table.delete_item(Key={
            'name': name,
            'timestamp': timestamp,
        })

    def delete_comment_table(self):
        """Delete the comment table."""
        # self.table.delete()


if __name__ == '__main__':
    co = Comment()
    co.delete_one_comment('Hell', '2020-12-28 12:27:22')
    # all = co.load_all_comments()
    # print(all)
    # co.delete_all_comments()