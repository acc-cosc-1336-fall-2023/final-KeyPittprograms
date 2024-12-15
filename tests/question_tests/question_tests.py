#Question 4 tests

import unittest

from src.question_d.question_d import get_most_likely_ancestor_consensus

class Test_Config(unittest.TestCase):

    def test_get_most_likely_ancestor_consensus(self):
        string = "GATATATGCATATACTT"
        substring = "ATAT"
        self.assertEqual([2, 4, 10], get_most_likely_ancestor_consensus(string, substring))

