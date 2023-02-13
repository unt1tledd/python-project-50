import json
import yaml


def conversed(data):
    correct_values = {None: 'null', True: 'true', False: 'false'}
    for k, v in data.items():
        if isinstance(v, dict):
            conversed(v)
        elif isinstance(v, (bool, type(None))):
            data[k] = correct_values[v]
    return data


def reading_file(filepath):
    if filepath[-2:] == 'ml':
        file = yaml.safe_load(open(filepath))
    elif filepath[-4:] == 'json':
        file = json.load(open(filepath))
    else:
        raise Exception("Unsupported type of file")
    return file
