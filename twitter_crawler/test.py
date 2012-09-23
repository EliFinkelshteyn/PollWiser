__author__ = 'bill.yang'

import sys
import simplejson as json
import shelve
from dateutil import parser


def tweet_for_candidate(db):
    dated_dict = dict()
    for key, item in db.items():
        dataDate = parser.parse(item['created_at']).date()
        if dataDate not in dated_dict:
            dated_dict[dataDate] = []
        dated_dict[dataDate].append(item)

    for key in sorted(dated_dict.keys()):
        obama_items = [item for item in dated_dict[key] if 'obama' in item['text'].lower()]
        romney_items = [item for item in dated_dict[key] if 'romney' in item['text'].lower()]

        print("%s has %d tweets" % (str(key), len(dated_dict[key])))
        print("%d Obama tweets, %d Romney tweets" % (len(obama_items), len(romney_items)))
        print("%d Obama popular tweets, %d Romney popular tweets" % (popular_tweet(obama_items), popular_tweet(romney_items)))

def popular_tweet(items):
    count = 0
    for item in items:
        result_type = item['metadata']['result_type']
        if result_type == 'popular':
            count +=1

    return count


db = shelve.open('result.shelve')
print('total popular tweet %d' % popular_tweet([value for key, value in db.items()]))
tweet_for_candidate(db)