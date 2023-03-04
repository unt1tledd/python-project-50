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
    extension = filepath.split('.')
    if extension[1] == 'yaml' or extension[1] == 'yml':
        file = reading_yaml(filepath)
    elif extension[1] == 'json':
        file = reading_json(filepath)
    else:
        raise Exception("Unsupported type of file")
    return file


def reading_yaml(filepath):
    file = yaml.safe_load(open(filepath))
    return file


def reading_json(filepath):
    file = json.load(open(filepath))
    return file
