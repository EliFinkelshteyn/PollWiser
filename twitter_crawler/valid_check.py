
import simplejson as json
from dateutil import parser

testFile = json.load(open('data/obama.json', 'r'))

print testFile[1]['text']
print testFile[1]['created_at']
print parser.parse(testFile[1]['created_at']).date()