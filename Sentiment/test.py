import shelve

__author__ = 'bill.yang'


parsed_data = shelve.open('parsed.shelve')

for key, value in parsed_data['data'].items():
    print key
    print('Candidate \t Negative \t Positive')
    non_neutral_count = value['obama_count'] - value['obama_sentiments'][1]

    obama_sentiment_percents = [sent_count * 1.0 / (non_neutral_count if non_neutral_count > 0 else 1) * 100 for sent_count in value['obama_sentiments']]
    print('Obama \t\t %.1f \t\t %.1f' % (obama_sentiment_percents[0], obama_sentiment_percents[2]))

    non_neutral_count = value['romney_count'] - value['romney_sentiments'][1]

    romney_sentiment_percents = [sent_count * 1.0 / (non_neutral_count if non_neutral_count > 0 else 1) * 100 for sent_count in value['romney_sentiments']]
    print('Romney \t\t %.1f \t\t %.1f' % (romney_sentiment_percents[0], romney_sentiment_percents[2]))

    print('Obama Popular Tweets: %d' % len(value['obama_popular_tweets']))
    print('Romney Popular Tweets: %d' % len(value['romney_popular_tweets']))
