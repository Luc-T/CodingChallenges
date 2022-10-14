import unittest
import karacas


class TestEncryption(unittest.TestCase):

    def test_numlength(self):
        self.assertEqual(karacas.encrypt("karaca"), "0c0r0kaca")
        self.assertEqual(karacas.encrypt("burak"), "k0r3baca")
        self.assertEqual(karacas.encrypt("banana"), "0n0n0baca")
        self.assertEqual(karacas.encrypt("alpaca"), "0c0pl0aca")

if __name__ == '__main__':
    unittest.main()