
import simplejson as json
from dateutil import parser

class Features:
    raw_data = None
    dated_data_dict = dict()

    def __init__(self, rawJsonObj):
        self.raw_data = rawJsonObj
        for i in xrange(len(self.raw_data)):
            dataDate = parser.parse(self.raw_data[i]['created_at']).date()
            if dataDate not in self.dated_data_dict:
                self.dated_data_dict[dataDate] = []

            self.dated_data_dict[dataDate].append(rawJsonObj[i])


    def num_word_count(self, name, date):
        return len([item for item in self.dated_data_dict[date] if name in item['text']])


