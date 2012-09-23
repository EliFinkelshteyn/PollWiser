import shelve

__author__ = 'bill.yang'


data = shelve.open('sentiment_result.shelve')

print len(data)