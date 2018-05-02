import os
import json


class DeepManagerHelper:
    @staticmethod
    def input(path):
        return os.path.join("input", path)

    @staticmethod
    def output(path):
        return os.path.join("output", path)

    @staticmethod
    def _to_json(obj):
        try:
            return json.dumps(obj)
        except:
            return "{}"

    @staticmethod
    def log(**kwargs):
        print("@deepmanager", DeepManagerHelper._to_json(kwargs), flush=True)
