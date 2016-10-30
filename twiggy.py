# -*- coding: utf-8 -*-

import datetime
import sys
import time

import tweepy

from access import ACCESS_TOKEN, ACCESS_TOKEN_SECRET
from consumer import CONSUMER_KEY, CONSUMER_SECRET

# Read CLI parameters
argfile = str(sys.argv[1])
argmode = str(sys.argv[2])

# Twitter authentication
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Open text file
filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

# TODO: check messages length

for line in f:
    # Take date and tweet
    thyme, text = line.split(' ', 1)

    # If time check is active
    if (argmode == "time"):
        time_from_text = datetime.datetime.strptime(thyme, '%Y-%m-%d_%H:%M')
        # Wait until is not his time
        while (time_from_text > datetime.datetime.now()):
            time.sleep(60)
        # Send tweet
        api.update_status(status=text)

    # If not time check is active
    else:
        # Send tweet
        api.update_status(status=text)

    # Anyway after send tweet wait for 15 mins
    time.sleep(900)
