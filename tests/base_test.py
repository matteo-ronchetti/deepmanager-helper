import sys
import os
import unittest
import json
import io

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

        captured = io.StringIO()  # Create StringIO object
        sys.stdout = captured  # and redirect stdout.
        DeepManagerHelper.log(accuracy=0.3234)  # Call function.
        sys.stdout = sys.__stdout__  # Reset redirect.
        
        self.assertEqual("@deepmanager "+json.dumps(obj)+"\n", captured.getvalue())

