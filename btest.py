import unittest
#from mypackage import func

def func(n):
    return n * n


class TestFunc(unittest.TestCase):
    def test_simple_cases(self):
        for c, a in (1, 1), (2, 4), (3, 9):
            self.assertEqual(func(c), a)
            
if __name__ == '__main__':
    unittest.main()
