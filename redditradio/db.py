import json
import os


FILENAME = 'post_ids.json'


class PostIDAlreadyExistsException(Exception):
    pass


def init_post_ids_db():
    if not os.path.isfile(FILENAME):
        open(FILENAME, 'w+').write('[]')


def get_post_ids_db():
    init_post_ids_db()

    return json.loads(open(FILENAME).read())


def add_post_id(post_id):
    db = get_post_ids_db()

    if post_id in db:
        raise PostIDAlreadyExistsException

    db.append(post_id)

    return open(FILENAME, 'w+').write(json.dumps(db))
