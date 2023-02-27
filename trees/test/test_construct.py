import unittest

from trees.ConstructQuadTree import construct


class MyTestCase(unittest.TestCase):
    def test_construct(self):
        root = construct(self, [[0, 1], [1, 0]])

        self.assertEqual(0, root.top_left.val)
        self.assertEqual(1, root.top_right.val)
        self.assertEqual(1, root.bottom_left.val)
        self.assertEqual(0, root.bottom_right.val)

    def test_construct_1(self):
        root = construct(self, [
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0],
            [1, 1, 1, 1, 0, 0, 0, 0]
        ])

        self.assertEqual(1, root.top_left.val)
        self.assertEqual(1, root.top_right.val)
        self.assertEqual(1, root.bottom_left.val)
        self.assertEqual(0, root.bottom_right.val)

        self.assertEqual(0, root.top_right.top_left.val)
        self.assertEqual(0, root.top_right.top_right.val)
        self.assertEqual(1, root.top_right.bottom_left.val)
        self.assertEqual(1, root.top_right.bottom_right.val)


if __name__ == '__main__':
    unittest.main()
