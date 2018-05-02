import sys
import os
import unittest

# pylint: disable=wrong-import-order,wrong-import-position
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import deepmanagerhelper as dmh


class BaseTest(unittest.TestCase):
    def test_nothing(self):
        self.assertEqual(2, 1+1)