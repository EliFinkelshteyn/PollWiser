import codecs
import shelve

__author__ = 'bill.yang'

import requests
import simplejson as json

def create_bulk_data_list(result_shelve):
    source_db = shelve.open('source.shelve')

    data_list = []
    data = {'data':[]}
    count = 0
    for key, item in source_db.items():
        if key not in result_shelve:
            data['data'].append({'text': item['text'], 'id': item['id']})
            count += 1
            if count > 5000:
                count = 0
                data_list.append(json.dumps(data))
                data = {'data':[]}

    data_list.append(json.dumps(data))

    return data_list

def create_test_data():
    return ['{data: [{"text": "Hello World!", "id": 1}]}']


def run():
    result_shelve = shelve.open('sentiment_result.shelve')
    data_list = create_bulk_data_list(result_shelve)

    print('total of %d data sets\n' % len(data_list))
    process_index = 0
    for data in data_list:
        print('processing data set %d' % process_index)
        process_index += 1
        response = requests.post('http://www.sentiment140.com/api/bulkClassifyJson?appid=zz_fish@hotmail.com',data)
        print response.text
        response_json = json.loads(response.text)
        for item in response_json['data']:
            result_shelve[str(item['id'])] = item

        break


if __name__ == '__main__':
    run()
