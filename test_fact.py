import unittest
from functools import reduce

def factorize(x):
    """ Factorize positive integer and return its factors.
        :type x: int,>=0
        :rtype: tuple[N],N>0
    """
    if not isinstance(x, int):
        raise TypeError

    if not x >= 0:
        raise ValueError 

    if x == 0: return (0,)
    elif x == 1: return (1,)

    factors = []
    for f in range(2, x):
        if x % f == 0:
            combined = False
            for a in factors:
                for b in factors:
                    if a*b == f:
                        combined = True
            if not combined:
                factors.append(f)
            if reduce(lambda x, y: x*y, factors) == x:
                return tuple(factors)
    if len(factors) == 0:
        factors.append(x)

    while reduce(lambda x, y: x*y, factors) != x:
        factors.append(factors[0])
        i += 1

    return tuple(factors)

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
