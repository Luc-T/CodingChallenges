import DisariumNumbers as dm
import unittest

class TestDisariumNumbers(unittest.TestCase):

    def test_truedisariumnumbers(self):
        self.assertTrue(dm.is_disarium(135)) #fails, not done yet

    def test_falsedisariumnumbers(self):
        self.assertFalse(dm.is_disarium(75)) #fails, not done yet
        

if __name__ == '__main__':
    unittest.main()