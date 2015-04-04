# -*- coding: utf-8 -*-

import datetime
import sys
import time
import tweepy

from consumer import CONSUMER_KEY, CONSUMER_SECRET
from access import ACCESS_TOKEN, ACCESS_TOKEN_SECRET

# lettura parametri riga di comando
argfile = str(sys.argv[1])
argmode = str(sys.argv[2])

# autenticazione twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# apro il file di testo
filename=open(argfile,'r')
f=filename.readlines()
filename.close()

# todo controllo lunghezza

# per ogni riga del file...
for line in f:
    # dalla linea prendo la data e il testo
    thyme, text = line.split(' ', 1)
    
    # controllo il tempo
    if (argmode == "time"):
        time_from_text = datetime.datetime.strptime(thyme, '%Y-%m-%d_%H:%M')
        # se non è ancora arrivata la sua ora, aspetta...
        while (time_from_text > datetime.datetime.now()):
            time.sleep(60)
        #print text
        api.update_status(status=text)

    # se non controllo il tempo stampo il tweet
    else:
        #print text
        api.update_status(status=text)

    # in entrambi i casi aspetto 15 minuti
    time.sleep(900)
    
