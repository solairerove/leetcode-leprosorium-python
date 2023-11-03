import unittest

from heap.TopKFrequentWords import top_k_frequent_sorting, top_k_frequent_heap, top_k_frequent_bucket


class MyTestCase(unittest.TestCase):
    def test_top_k_frequent_words(self):
        actual = top_k_frequent_sorting(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=2)
        self.assertEqual(["i", "love"], actual)

        actual = top_k_frequent_heap(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=2)
        self.assertEqual(["i", "love"], actual)

        actual = top_k_frequent_bucket(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=2)
        self.assertEqual(["i", "love"], actual)

    def test_top_k_frequent_words_1(self):
        actual = top_k_frequent_sorting(self, words=["the", "day", "is", "sunny",
                                                     "the", "the",
                                                     "the", "sunny", "is", "is"], k=4)
        self.assertEqual(["the", "is", "sunny", "day"], actual)

        actual = top_k_frequent_heap(self, words=["the", "day", "is", "sunny",
                                                  "the", "the",
                                                  "the", "sunny", "is", "is"], k=4)
        self.assertEqual(["the", "is", "sunny", "day"], actual)

        actual = top_k_frequent_bucket(self, words=["the", "day", "is", "sunny",
                                                    "the", "the",
                                                    "the", "sunny", "is", "is"], k=4)
        self.assertEqual(["the", "is", "sunny", "day"], actual)

    def test_top_k_frequent_words_2(self):
        actual = top_k_frequent_sorting(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=3)
        self.assertEqual(["i", "love", "coding"], actual)

        actual = top_k_frequent_heap(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=3)
        self.assertEqual(["i", "love", "coding"], actual)

        actual = top_k_frequent_bucket(self, words=["i", "love", "leetcode", "i", "love", "coding"], k=3)
        self.assertEqual(["i", "love", "coding"], actual)


if __name__ == '__main__':
    unittest.main()
