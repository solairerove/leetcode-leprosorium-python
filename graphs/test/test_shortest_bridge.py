import unittest

from graphs.ShortestBridge import shortest_bridge


class MyTestCase(unittest.TestCase):
    def test_shortest_bridge(self):
        self.assertEqual(1, shortest_bridge(self, [[0, 1], [1, 0]]))

    def test_shortest_bridge_1(self):
        self.assertEqual(2, shortest_bridge(self, [[0, 1, 0], [0, 0, 0], [0, 0, 1]]))

    def test_shortest_bridge_2(self):
        self.assertEqual(1, shortest_bridge(self, [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1],
                                                   [1, 1, 1, 1, 1]]))


if __name__ == '__main__':
    unittest.main()
