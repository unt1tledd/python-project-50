import json
import yaml


def get_data(filepath):
    format = filepath.split('.')[1]
    if format == 'yaml' or format == 'yml' or format == 'json':
        file = open(filepath)
    else:
        raise Exception("Unsupported type of file")
    return file, format


def read_file(file, format):
    if format == 'json':
        file = json.load(file)
    else:
        file = yaml.safe_load(file)
    return file
