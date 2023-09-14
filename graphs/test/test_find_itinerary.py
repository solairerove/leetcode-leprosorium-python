import unittest

from graphs.ReconstructItinerary import find_itinerary


class MyTestCase(unittest.TestCase):
    def test_find_itinerary(self):
        self.assertEqual(["JFK", "MUC", "LHR", "SFO", "SJC"],
                         find_itinerary(self, [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))

    def test_find_itinerary_1(self):
        self.assertEqual(["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"], find_itinerary(self,
                                                                                    [["JFK", "SFO"], ["JFK", "ATL"],
                                                                                     ["SFO", "ATL"], ["ATL", "JFK"],
                                                                                     ["ATL", "SFO"]]))


if __name__ == '__main__':
    unittest.main()
