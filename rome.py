#!/usr/bin/env python

import tweepy, time, sys

#enter the corresponding information from your Twitter application:
#VoxPopulisMMXVI
CONSUMER_KEY = '123'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = '123'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '123-123'#keep the quotes, replace this with your access token
ACCESS_SECRET = '123'#keep the quotes, replace this with your access token secret


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

# compute how many seconds in a day
day = 60 * 60 * 24
max_tweet_length = 140
roman_facts = [
    'Pompey on trial for his posthumous fathers antics; judge likes Pompey so he offers his daughter Antistia in marriage. #acquitted #pompeyfacts'
    'Sulla, consul pre-Pompey, persuaded Pomey to divorce Antistia in favour of his step-daughter Aemilia. Very crafty Sulla. #pompeyfacts',
    'In 81 BCE Pomey attempted a triumph with 4 elephants brought from Africa. Unfortunately the porta triumphalis was too narrow. #pompeyfacts',
    'Around 65 BCE Pompey joined Crassus and Caesar in the unofficial military-political alliance known as the First Triumvirate. #pompeyfacts',
]
sanitised = []


# remove any facts that are greater than 140 characters, and print the fact
for line in roman_facts:
    if len(line) > max_tweet_length:
        print('- Tweet length exceed max length: {0}: {1}'.format(len(line), line))
    else:
        print('- Tweet length is good: {0}: {1}'.format(len(line), line))
        sanitised.append(line)

        
# switch the original list to the sanitised one
roman_facts = sanitised



print('- About to tweet {0} facts'.format(len(roman_facts)))

for line in roman_facts:
    #api.update_status(line)
    print('- Done tweeting: \'{0}\''.format(line))
    
    # sleep a day before posting the next fact
    print('- Slepping for {0} seconds'.format(day))
    time.sleep(day)

print('- Done tweeting all facts')
