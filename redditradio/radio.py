from google_speech import Speech
import json
import requests
from user_agent import generate_user_agent
import redditradio.db as db


def say(text, speed=1.5, lang='en'):
    try:
        speech = Speech(text.replace('\n', ''), lang)
        speech.play()

        sox_effects = ('speed', speed)
        speech.play(sox_effects)
    except TypeError:
        print('Could not read {}'.format(text))


def read_post(post):
    say('Here is a post by {}'.format(post['data']['author']))
    say(post['data']['title'])
    say(post['data']['selftext'])


def stream_channel(channel):
    ua = generate_user_agent()

    def fetch_and_read_new_posts():
        new_posts = json.loads(
            requests.get(
                'https://www.reddit.com/r/{}/.json'.format(channel),
                headers={'User-Agent': ua}
            ).text
        )['data']['children']

        for post in new_posts:
            if post['data']['id'] not in db.get_post_ids_db():
                read_post(post)

                try:
                    db.add_post_id(post['data']['id'])
                except db.PostIDAlreadyExistsException:
                    continue

    while True:
        fetch_and_read_new_posts()
