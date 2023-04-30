import unittest

from def_for_unittest_hw14 import prime_factors_of_number


class TestPrimeFactors(unittest.TestCase):

    def test_prime_number(self):
        self.assertEqual(prime_factors_of_number(1), "Число является простым")

    def test_composite_number(self):
        self.assertEqual(prime_factors_of_number(10), [2, 5])

    def test_not_number(self):
        self.assertRaises(TypeError, prime_factors_of_number, 'gfhd')
            

if __name__ == '__main__':
    unittest.main(verbosity=2)