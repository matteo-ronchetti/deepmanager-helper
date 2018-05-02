import sys
import os
import unittest
import json

# pylint: disable=wrong-import-order,wrong-import-position
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from deepmanagerhelper import DeepManagerHelper


class BaseTest(unittest.TestCase):
    def test_io(self):
        self.assertEqual("input/file", DeepManagerHelper.input("file"))
        self.assertEqual("output/file", DeepManagerHelper.output("file"))

    def test_logging(self):
        obj = {"accuracy": 0.3234}
        self.assertEqual(json.dumps(obj), DeepManagerHelper._to_json(obj))
        self.assertEqual("{}", DeepManagerHelper._to_json(self))
