__author__ = 'EliFinkelshteyn'
from firebase import Firebase
import simplejson as json
f = Firebase('http://demo.firebase.com/seifeet/twitter_data')
for item in json.load(open('../Data/obama.json')):
    if isinstance(item,dict):
        print 'about to push!'
        f.push(item)
        print 'done!'