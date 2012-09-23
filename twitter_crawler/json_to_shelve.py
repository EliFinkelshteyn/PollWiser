# json to shelve converter
import shelve
import simplejson as json

__author__ = 'bill.yang'



f = open('data/result.json', 'r')
db = shelve.open('result.shelve')

for line in f.readlines():
    line_item = json.loads(line.rstrip().rstrip(','))
    db[str(line_item['id'])] = line_item

db.close()