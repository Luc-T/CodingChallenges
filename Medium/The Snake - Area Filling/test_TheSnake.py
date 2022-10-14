import unittest
import TheSnake

class TestEncryption(unittest.TestCase):

    def test_snakeeating(self):
        self.assertEqual(TheSnake.snakefill(3), 3)
        self.assertEqual(TheSnake.snakefill(6), 5)
        self.assertEqual(TheSnake.snakefill(24), 9)
        self.assertEqual(TheSnake.snakefill(555), 18)
        

if __name__ == '__main__':
    unittest.main()