import shelve
import simplejson as json
from firebase import Firebase
from dateutil import parser
from time import mktime

__author__ = 'bill.yang'

def parse_tweets(tweet_db, sentiment_db):
    dated_dict = dict()
    for key, item in tweet_db.items():
        dataDate = str(parser.parse(item['created_at']).date())
        if dataDate not in dated_dict:
            dated_dict[dataDate] = []
        dated_dict[dataDate].append(item)

    result = {}
    for key in sorted(dated_dict.keys()):
        obama_tweets = [item for item in dated_dict[key] if 'obama' in item['text'].lower()]
        romney_tweets = [item for item in dated_dict[key] if 'romney' in item['text'].lower()]

        day_count = len(dated_dict[key])
        obama_count = len(obama_tweets)
        romney_count = len(romney_tweets)
        obama_popular_tweets = popular_tweet(obama_tweets)
        romney_popular_tweets = popular_tweet(romney_tweets)
        obama_tweets_ids = [item['id'] for item in obama_tweets]
        romney_tweets_ids = [item['id'] for item in romney_tweets]
        obama_sentiment_items = [s_item for s_key, s_item in sentiment_db.items() if s_item['id'] in obama_tweets_ids]
        romney_sentiment_items = [s_item for s_key, s_item in sentiment_db.items() if s_item['id'] in romney_tweets_ids]

        print("%s has %d tweets" % (str(key), day_count))
        print("%d Obama tweets, %d Romney tweets" % (obama_count, romney_count))

        result[key] = { 'date' : int(mktime(parser.parse(key).timetuple())),
                        'day_count': day_count,
                        'obama_count' : obama_count,
                        'romney_count': romney_count,
                        'obama_popular_tweets': obama_popular_tweets,
                        'romney_popular_tweets': romney_popular_tweets,
                        'obama_sentiments': get_sentiment(obama_sentiment_items),
                        'romney_sentiments': get_sentiment(romney_sentiment_items)}

    return result

def popular_tweet(items):
    result = []
    for item in items:
        result_type = item['metadata']['result_type']
        if result_type == 'popular':
            result.append(item)

    return result

def get_sentiment(items):
    # result is count for [negative, neutral, positive]
    result = [0, 0, 0]
    for item in items:
        result[item['polarity']/2] += 1

    return result


tweet_db = shelve.open('source.shelve')
sentiment_db = shelve.open('sentiment_result.shelve')

parsed_data = parse_tweets(tweet_db, sentiment_db)

parsed_db = shelve.open('parsed.shelve')
parsed_db['data'] = parsed_data
parsed_db.sync()
