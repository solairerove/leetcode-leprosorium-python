import unittest

from dynamic_programming.PredictTheWinner import predict_the_winner


class MyTestCase(unittest.TestCase):
    def test_predict_the_winner(self):
        self.assertEqual(False, predict_the_winner(self, nums=[1, 5, 2]))

    def test_predict_the_winner_1(self):
        self.assertEqual(True, predict_the_winner(self, nums=[1, 5, 233, 7]))


if __name__ == '__main__':
    unittest.main()
