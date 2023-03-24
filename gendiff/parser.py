import json
import yaml


def get_data(filepath):
    format = filepath.split('.')[1]
    if format == 'yaml' or format == 'yml':
        file = yaml.safe_load(open(filepath))
    elif format == 'json':
        file = json.load(open(filepath))
    else:
        raise Exception("Unsupported type of file")
    return file
