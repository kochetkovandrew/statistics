import unittest
from src.statistics_bioresearch import kaerber, kaerber_ci


class KaerberTestCase(unittest.TestCase):

    def setUp(self):
        return

    def test_kaerber(self):
        """
        Test Kaerber titration method
        """
        titer = kaerber(0.125, 0.5, 4, [0, 0, 1, 3, 3, 4, 4])
        self.assertAlmostEqual(titer, 1/54, 2)

    def test_kaerber_ci(self):
        """
        Test Kaerber titration method
        """
        titer = kaerber_ci(0.125, 0.5, 4, [0, 0, 1, 3, 3, 4, 4])
        self.assertLess(titer['lower'], titer['titer'])
        self.assertLess(titer['titer'], titer['upper'])


if __name__ == '__main__':
    unittest.main()
