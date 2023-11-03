import unittest

from heap.TopKFrequentWords import top_k_frequent_sorting


class MyTestCase(unittest.TestCase):
    def test_top_k_frequent_words(self):
        self.assertEqual(["i", "love"],
                         top_k_frequent_sorting(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=2))

    def test_top_k_frequent_words_1(self):
        self.assertEqual(["the", "is", "sunny", "day"], top_k_frequent_sorting(self,
                                                                               words=["the", "day", "is", "sunny",
                                                                                      "the", "the",
                                                                                      "the", "sunny", "is", "is"], k=4))

    def test_top_k_frequent_words_2(self):
        self.assertEqual(["i", "love", "coding"], top_k_frequent_sorting(self,
                                                                         words=["i", "love", "leetcode", "i", "love",
                                                                                "coding"],
                                                                         k=3))


if __name__ == '__main__':
    unittest.main()
