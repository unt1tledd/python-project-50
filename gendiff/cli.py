import json
import yaml


def conversed(data):
    correct_values = {None: 'null', True: 'true', False: 'false'}
    if isinstance(data, (bool, type(None))):
        data = correct_values[data]
    return data


def reading_file(filepath):
    extension = filepath.split('.')
    if extension[1] == 'yaml' or extension[1] == 'yml':
        file = open(filepath)
        format = 'yaml'
    elif extension[1] == 'json':
        file = open(filepath)
        format = 'json'
    else:
        raise Exception("Unsupported type of file")
    return file, format


def parsed(file, format):
    if format == 'json':
        file = json.load(file)
    else:
        file = yaml.safe_load(file)
    return file


def read(filepath):
    with open(filepath) as f:
        file = f.read()
    return file
