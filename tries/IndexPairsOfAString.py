from typing import List


class TrieNode:
    def __init__(self):
        self.flag = False
        self.next = dict()


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for c in word:
            if c not in curr.next:
                curr.next[c] = TrieNode()
            curr = curr.next[c]
        curr.flag = True


# O(n * s + m^2) time || O(n * s) space
# m - text.length
# n - words.length
# s - average length of the words
def index_pairs(self, text: str, words: List[str]) -> List[List[int]]:
    trie = Trie()
    for word in words:
        trie.insert(word)

    res = []
    for i in range(len(text)):
        curr = trie.root
        for j in range(i, len(text)):
            if text[j] not in curr.next:
                break
            curr = curr.next[text[j]]

            if curr.flag:
                res.append([i, j])

    return res
