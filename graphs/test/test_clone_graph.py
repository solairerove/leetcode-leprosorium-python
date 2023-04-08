import unittest

from graphs.CloneGraph import clone_graph_dfs, Node, clone_graph_bfs


class MyTestCase(unittest.TestCase):
    def test_clone_graph(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)

        node1.neighbors = [node2, node4]
        node2.neighbors = [node1, node3]
        node3.neighbors = [node2, node4]
        node4.neighbors = [node3, node1]

        actual = clone_graph_dfs(self, node1)
        self.assertEqual(1, actual.val)
        self.assertEqual(2, actual.neighbors[0].val)
        self.assertEqual(4, actual.neighbors[1].val)

        actual = clone_graph_bfs(self, node1)
        self.assertEqual(1, actual.val)
        self.assertEqual(2, actual.neighbors[0].val)
        self.assertEqual(4, actual.neighbors[1].val)


if __name__ == '__main__':
    unittest.main()
