import json
import sys

# read file and return json data from file


def load_json_data(jsonfile):
    with open(jsonfile, 'r', buffering=-1) as myfile:
        data = myfile.read()
    obj = json.loads(data)
    return obj
