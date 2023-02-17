import unittest
from src.statistics_bioresearch import wilson


class WilsonTestCase(unittest.TestCase):

    def setUp(self):
        return

    def test_3_of_12(self):
        """
        Test Wilson CI for 3 positive results from a sample size of 12
        example values taken from https://www.statskingdom.com/proportion-confidence-interval-calculator.html
        """
        ci = wilson(3, 12)
        self.assertAlmostEqual(ci[0], 0.08894, 4)
        self.assertAlmostEqual(ci[1], 0.5323, 4)


if __name__ == '__main__':
    unittest.main()
