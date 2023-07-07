import unittest

from sliding_window.MaximizeTheConfusionOfAnExam import max_consecutive_answers


class MyTestCase(unittest.TestCase):
    def test_max_consecutive_answers(self):
        self.assertEqual(4, max_consecutive_answers(self, answer_key="TTFF", k=2))

    def test_max_consecutive_answers_1(self):
        self.assertEqual(3, max_consecutive_answers(self, answer_key="TFFT", k=1))

    def test_max_consecutive_answers_2(self):
        self.assertEqual(5, max_consecutive_answers(self, answer_key="TTFTTFTT", k=1))


if __name__ == '__main__':
    unittest.main()
