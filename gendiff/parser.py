import json
import yaml


def get_data(filepath):
    format = filepath.split('.')[1]
    file = open(filepath)
    return file, format


def reading_file(file, format):
    if format == 'json':
        file = json.load(file)
    elif format == 'yaml' or format == 'yml':
        file = yaml.safe_load(file)
    else:
        raise Exception("Unsupported type of file")
    return file
