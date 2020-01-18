import json


def read_Config(pat2file):
    with open(pat2file, "r") as read_file:
        json_string = json.load(read_file)
        return json_string  # dict
