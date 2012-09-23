
import simplejson as json
import codecs
import csv

code = 'utf-8'
source_data = json.load(codecs.open('source.json', 'r', encoding=code))

output_file = codecs.open('broken_result.csv', 'wb', encoding=code)

for item in source_data:
    output_file.write( item['text'] + '\n' );

output_file.close()