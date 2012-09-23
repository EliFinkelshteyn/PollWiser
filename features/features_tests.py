
import unittest
import simplejson as json
from dateutil import parser
from features import Features

class TestNumWordCount(unittest.TestCase):
    testData = []
    def setUp(self):
        self.testData = json.load(open('NumCandidateMentions.data', 'r'))

    def test_correct_mentions_count(self):
        features = Features(self.testData)
        count = features.num_word_count('Obama', parser.parse('Sep 21, 2012').date())
        self.assertEqual(2, count)

class Test


if __name__ == '__main__':
    unittest.main()
