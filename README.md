PollWiser
======================
This project is winner of [Dataweek](http://dataweek.co) hackathon in 2012.
PollWiser produces social context for poll results.


Getting Started
======================
There are several steps involved before PollWiser can be used.

## prepare twitter data
1. crawl twitter history using twitter_crawler/crawler.py

    Currently, the crawler is not fully autonomous, due to the fact we're using the free search API and not firehose.
    You need to modify the two lines setting search api url and change the dates to the target date + 1 (i.e. to crawl tweets from Sept 26, you need to change the date to 2012-09-27)
    And to crawl another day, you have to modify the date in the url every time, the crawler works incrementally.
    
1. the crawler will generate result.shelve file, copy this file to Sentiment directory and rename it as source.result.
    
1. generate sentiment result for crawled data by running Sentiment/sentiment.py

1. sentiment.py will generate a file called sentiment_result.shelve

1. run parse_result.py, this will generate a file called parsed.shelve based on source.shelve and sentiment_result.shelve

1. copy parsed.shelve to FirebaseUploader directory and rename it to parsed.data

1. go to firebase data store in browser and delete tweeter_data_2

1. run FirebaseParsedTweetUploader.py to upload parsed.data

## prepare poll data

TODO: add steps for preparing poll data