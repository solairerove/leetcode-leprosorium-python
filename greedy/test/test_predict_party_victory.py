import unittest

from greedy.Dota2Senate import predict_party_victory


class MyTestCase(unittest.TestCase):
    def test_predict_party_victory(self):
        self.assertEqual("Radiant", predict_party_victory(self, "RD"))

    def test_predict_party_victory_1(self):
        self.assertEqual("Dire", predict_party_victory(self, "RDD"))


if __name__ == '__main__':
    unittest.main()
