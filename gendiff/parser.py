import json
import yaml


def get_data(filepath):
    format = filepath.split('.')[1]
    if format == 'yaml' or format == 'yml':
        file = yaml.safe_load(file)
    elif format == 'json':
        file = json.load(file)
    else:
        raise Exception("Unsupported type of file")
    return file
