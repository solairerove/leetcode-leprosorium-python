import unittest

from stack.ValidateStackSequences import validate_stack_sequences_using_stack


class MyTestCase(unittest.TestCase):
    def test_validate_stack_sequences(self):
        self.assertEqual(True, validate_stack_sequences_using_stack(self, [1, 2, 3, 4, 5], [4, 5, 3, 2, 1]))

    def test_validate_stack_sequences_1(self):
        self.assertEqual(False, validate_stack_sequences_using_stack(self, [1, 2, 3, 4, 5], [4, 3, 5, 1, 2]))


if __name__ == '__main__':
    unittest.main()
