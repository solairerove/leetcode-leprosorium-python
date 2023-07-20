import unittest

from arrays.AsteroidCollision import asteroid_collision


class MyTestCase(unittest.TestCase):
    def test_asteroid_collision(self):
        self.assertEqual([5, 10], asteroid_collision(self, asteroids=[5, 10, -5]))

    def test_asteroid_collision_1(self):
        self.assertEqual([], asteroid_collision(self, asteroids=[8, -8]))

    def test_asteroid_collision_2(self):
        self.assertEqual([10], asteroid_collision(self, asteroids=[10, 2, -5]))


if __name__ == '__main__':
    unittest.main()
