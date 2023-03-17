import unittest

from tries.ImplementTrie import Trie


class MyTestCase(unittest.TestCase):
    def test_implement_trie(self):
        trie = Trie()
        trie.insert("apple")
        self.assertEqual(True, trie.search("apple"))
        self.assertEqual(False, trie.search("app"))
        self.assertEqual(True, trie.starts_with("app"))
        trie.insert("app")
        self.assertEqual(True, trie.search("app"))


if __name__ == '__main__':
    unittest.main()
