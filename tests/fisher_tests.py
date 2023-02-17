import unittest
from src.statistics_bioresearch import fisher


class FisherTestCase(unittest.TestCase):

    def setUp(self):
        return

    def test_1_of_20(self):
        """
        Test Fisher CI for 1 positive results from a sample size of 20
        """
        ci = fisher(1, 20)
        self.assertAlmostEqual(ci[0], 4.0687824488498645e-05, 4)
        self.assertAlmostEqual(ci[1], 0.1850, 4)

    def test_450_of_1000(self):
        """
        Test Fisher CI for 450 positive results from a sample size of 1000
        example values taken from http://medstatistic.ru/articles/doveritelnye-intervaly-dlya-chastot-i-doley.pdf
        """
        ci = fisher(450, 1000)
        self.assertAlmostEqual(ci[0], 0.4193, 4)
        self.assertAlmostEqual(ci[1], 0.4809, 4)


if __name__ == '__main__':
    unittest.main()
