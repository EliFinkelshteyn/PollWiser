
import simplejson as json
import codecs
import csv

code = 'utf-8'
source_data = json.load(codecs.open('source.json', 'r', encoding=code))

output_file = codecs.open('broken_result.csv', 'wb', encoding=code)

for item in source_data:
    line = item['text'].replace('"', '""').replace('=','')
    output_file.write( '"' + line  + '"\n' )

output_file.close()