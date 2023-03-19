import unittest

from tries.DesignAddAndSearchWordsDataStructure import WordDictionary


class MyTestCase(unittest.TestCase):
    def test_words_data_structure(self):
        word_dictionary = WordDictionary()
        word_dictionary.add_word("bad")
        word_dictionary.add_word("dad")
        word_dictionary.add_word("mad")
        self.assertEqual(False, word_dictionary.search("pad"))
        self.assertEqual(True, word_dictionary.search("bad"))
        self.assertEqual(True, word_dictionary.search(".ad"))
        self.assertEqual(True, word_dictionary.search("b.."))


if __name__ == '__main__':
    unittest.main()
