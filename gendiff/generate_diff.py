from gendiff.cli import reading_file, parsed
from gendiff.maker_diff import make_diff
from gendiff.formatters.stylish import stylish_format
from gendiff.formatters.plain import plain_format
from gendiff.formatters.json import json_format


def generate_diff(filepath1, filepath2, name='stylish'):
    file1, format = reading_file(filepath1)
    file1 = parsed(file1, format)
    file2, format = reading_file(filepath2)
    file2 = parsed(file2, format)
    diff = make_diff(file1, file2)
    if name == 'stylish':
        diff = f"{{\n{stylish_format(diff)}}}\n"
    elif name == 'plain':
        diff = plain_format(diff)
    elif name == 'json':
        diff = json_format(diff)
    else:
        raise ValueError('This format is not supported:(')
    return diff
