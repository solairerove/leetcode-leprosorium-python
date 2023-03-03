import unittest

from arrays.GroupAnagrams import group_anagrams, group_anagrams_count_approach


class MyTestCase(unittest.TestCase):
    def test_group_anagrams(self):
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
                         group_anagrams(self, ["eat", "tea", "tan", "ate", "nat", "bat"]))

        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']],
                         group_anagrams_count_approach(self, ["eat", "tea", "tan", "ate", "nat", "bat"]))


if __name__ == '__main__':
    unittest.main()
