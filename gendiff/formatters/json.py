import json


def json_format(diff):
    dict(diff)
    return json.dumps(diff, indent=4)
