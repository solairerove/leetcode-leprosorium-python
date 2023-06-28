import unittest

from graphs.PathWithMaximumProbability import max_probability_bellman_ford, max_probability_dijkstra


class MyTestCase(unittest.TestCase):
    def test_max_probability(self):
        self.assertEqual(0.25000,
                         max_probability_bellman_ford(self, n=3, edges=[[0, 1], [1, 2], [0, 2]],
                                                      succ_prob=[0.5, 0.5, 0.2], start=0,
                                                      end=2))
        self.assertEqual(0.25000,
                         max_probability_dijkstra(self, n=3, edges=[[0, 1], [1, 2], [0, 2]],
                                                  succ_prob=[0.5, 0.5, 0.2], start=0,
                                                  end=2))

    def test_max_probability_1(self):
        self.assertEqual(0.30000,
                         max_probability_bellman_ford(self, n=3, edges=[[0, 1], [1, 2], [0, 2]],
                                                      succ_prob=[0.5, 0.5, 0.3], start=0,
                                                      end=2))
        self.assertEqual(0.30000,
                         max_probability_dijkstra(self, n=3, edges=[[0, 1], [1, 2], [0, 2]],
                                                  succ_prob=[0.5, 0.5, 0.3], start=0,
                                                  end=2))

    def test_max_probability_2(self):
        self.assertEqual(0.00000,
                         max_probability_bellman_ford(self, n=3, edges=[[0, 1]], succ_prob=[0.5], start=0, end=2))

        self.assertEqual(0.00000,
                         max_probability_dijkstra(self, n=3, edges=[[0, 1]], succ_prob=[0.5], start=0, end=2))


if __name__ == '__main__':
    unittest.main()
