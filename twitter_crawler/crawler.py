import shelve
import traceback
import requests
import simplejson as json
import time
import sys

def craw_url(db, response):
    jsonObj = json.loads(response.text)
    for tweet_json in jsonObj['results']:
        if str(tweet_json['id']) in db:
            #print 'skipped tweet id ' + str(tweet_json['id'])
            pass
        else:
            db[str(tweet_json['id'])] = tweet_json
            #print 'added tweet id ' + str(tweet_json['id'])

def run():
    page = int(sys.argv[1]) if len(sys.argv) > 1 else 1
    db = shelve.open('result.shelve')

    for i in range(15):
        try:
            url = 'http://search.twitter.com/search.json?q=obama&rpp=100&include_entities=true&result_type=mixed&until=2012-09-15&page='+str(page)
            response = requests.get(url)
            craw_url(db, response)

            url = 'http://search.twitter.com/search.json?q=romney&rpp=100&include_entities=true&result_type=mixed&until=2012-09-15&page='+str(page)
            response = requests.get(url)
            craw_url(db, response)

            db.sync()
            print('processed page %d, total tweets %d' % (page, len(db)))
            page += 1;

            time.sleep(10)
        except:
            print '===Error Begin'
            print response.text
            print url
            print '===Error End'
            if response.text != '{"error":"Invalid query"}':
                print 'FAILED'
                traceback.print_exception()
                break

    db.close()

if __name__ == '__main__':
    run()
