# -*- coding: utf-8 -*-
import datetime
import logging
import sys
import time

import click
import tweepy

from config import LEVEL, CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


@click.command()
@click.option('--source', help='The source file of the tweets', required=True)
@click.option('--mode', help='Choose time only if your source uses time', required=True, type=click.Choice(['time', 'notime']))
def main(source, mode):
    # Twitter authentication
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    logging.info('Authentication completed')

    # Read text file
    filename = open(source, 'r')
    f = filename.readlines()
    filename.close()
    logging.info('Source file read')

    # TODO: check messages length

    for line in f:
        tweet_time, tweet_text = line.split(' ', 1)

        # Time check
        if mode == 'time':
            date_from_text = datetime.datetime.strptime(tweet_time, '%Y-%m-%d_%H:%M')
        else:
            date_from_text = datetime.datetime.strptime(tweet_time, '%Y-%m-%d')
        while date_from_text > datetime.datetime.now():
            time.sleep(60)

        # Send tweet
        api.update_status(status=tweet_text)
        logging.info('Sent {}'.format(tweet_text))
        time.sleep(60)


if __name__ == '__main__':
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(stream=sys.stdout, level=LEVEL, format=log_format)
    main()
