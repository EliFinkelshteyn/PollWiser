__author__ = 'EliFinkelshteyn'
from firebase import Firebase
import simplejson as json
import datetime

#"Fri, 21 Sep 2012 16:53:08 +0000"
def getTwitterDate(date):
    date = date[:-6]
    date = datetime.datetime.strptime(date, '%a, %d %b %Y %H:%M:%S')
    date += datetime.timedelta( 0, -7*60*60)
    return date.strftime('%s')

f = Firebase('http://demo.firebase.com/seifeet/twitter_data')
for item in json.load(open('../Data/romney.json')):
    if isinstance(item,dict):
        item['date'] = getTwitterDate(item['created_at'])
        print 'about to push!'
        f.push(item)
        print 'done!'