
import requests
import simplejson as json
import time

obamaFile = open('obama.json', 'a')
romneyFile = open('romney.json', 'a')
obamaFile.write('["start"')
romneyFile.write('["start"')
page = 1
while page < 100:
    r = requests.get('http://search.twitter.com/search.json?q=obama&rpp=100&include_entities=true&result_type=mixed&page='+str(page))
    jsonObj = json.loads(r.text)
    buffer = ',' + json.dumps(jsonObj["results"]).strip('[').strip(']')
    obamaFile.write(buffer)
    print buffer

    r = requests.get('http://search.twitter.com/search.json?q=romney&rpp=100&include_entities=true&result_type=mixed&page='+str(page))
    jsonObj = json.loads(r.text)
    buffer = ',' + json.dumps(jsonObj["results"]).strip('[').strip(']')
    romneyFile.write(buffer)
    print buffer

    print 'processed page ' + str(page)
    page += 1
    time.sleep(0.1)


obamaFile.write(']')
romneyFile.write(']')

obamaFile.close()
romneyFile.close()