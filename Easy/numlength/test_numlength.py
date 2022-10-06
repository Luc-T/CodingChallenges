import unittest
import numlength


class TestNumLen(unittest.TestCase):

    def test_numlength(self):
        self.assertEqual(numlength.number_length(10), 2)
        self.assertEqual(numlength.number_length(5000), 4)
        self.assertEqual(numlength.number_length(0), 1)
        self.assertEqual(numlength.number_length(4039182), 7)
        self.assertEqual(numlength.number_length(9999999999999999), 16)
        self.assertEqual(numlength.number_length(1), 1)
        self.assertEqual(numlength.number_length(
            777777777777777777777777777777), 30)

if __name__ == '__main__':
    unittest.main()