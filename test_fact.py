import unittest

def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError

    if not x >= 0:
        raise ValueError 


class TestFactorize(unittest.TestCase):
    def test_wrong_types_raise_exception(self):
        with self.subTest(x=1):
            self.assertRaises(TypeError, factorize, 'Hello',
                    msg='String argument not raising TypeError')
        with self.subTest(x=1):
            self.assertRaises(TypeError, factorize, 1.5,
                    msg='Float argument not raising TypeError')

    def test_negative(self):
        with self.subTest(x=1):
            self.assertRaises(ValueError, factorize, -1)
        with self.subTest(x=2):
            self.assertRaises(ValueError, factorize, -10)
        with self.subTest(x=3):
            self.assertRaises(ValueError, factorize, -100)

    def test_zero_and_one_cases(self):
        with self.subTest(x=0):
            self.assertEqual(factorize(0), (0,))
        with self.subTest(x=1):
            self.assertEqual(factorize(1), (1,))

    def test_simple_numbers(self):
        with self.subTest(x=1):
            self.assertEqual(factorize(3), (3,))
        with self.subTest(x=2):
            self.assertEqual(factorize(13), (13,))
        with self.subTest(x=3):
            self.assertEqual(factorize(29), (29,))

    def test_two_simple_multipliers(self):
        cases = [(6, (2, 3)), (26, (2, 13)), (121, (11, 11))]
        for n, fact_n in cases:
            with self.subTest(x=n):
                self.assertEqual(factorize(n), fact_n)

    def test_many_multiplyers(self):
        cases = [(1001, (7, 11, 13)), 
                (9699690, (2, 3, 5, 7, 11, 13, 17, 19))]
        for n, fact_n in cases:
            with self.subTest(x=n):
                self.assertEqual(factorize(n), fact_n)


if __name__ == '__main__':
    unittest.main()
