import unittest

from arrays.EncodeAndDecodeStrings import encode, decode


class MyTestCase(unittest.TestCase):
    def test_test_encode_and_decode_strings(self):
        to_encode = ["Hello", "World"]
        encoded = encode(to_encode)
        actual = decode(encoded)

        self.assertEqual(to_encode, actual)

    def test_test_encode_and_decode_strings_1(self):
        to_encode = [""]
        encoded = encode(to_encode)
        actual = decode(encoded)

        self.assertEqual(to_encode, actual)


if __name__ == '__main__':
    unittest.main()
