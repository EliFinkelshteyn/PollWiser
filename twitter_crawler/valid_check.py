
import simplejson as json

testFile = json.load(open('obama.json', 'r'))

print testFile[1]['text']