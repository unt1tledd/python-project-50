import json


def json_format(diff):
    diff = dict(sorted(diff.items(), key=lambda x: x[0]))
    return json.dumps(diff, indent = 4)
