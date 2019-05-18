from redditradio.radio import stream_channel
import sys


def run():
    if len(sys.argv) < 2:
        print('Usage: redditradio <subreddit_name>')
        quit()

    stream_channel(sys.argv[1])
