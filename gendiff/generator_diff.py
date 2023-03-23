from gendiff.parser import get_data
from gendiff.maker_diff import make_diff
from gendiff.formatters.stylish import format_stylish
from gendiff.formatters.plain import format_plain
from gendiff.formatters.json import format_json


def formatted(format, diff):
    if format == 'stylish':
        diff = f"{{\n{format_stylish(diff)}}}"
    elif format == 'plain':
        diff = format_plain(diff)
    elif format == 'json':
        diff = format_json(diff)
    else:
        raise ValueError('This format is not supported:(')
    return diff


def generate_diff(filepath1, filepath2, format='stylish'):
    file1 = get_data(filepath1)
    file2 = get_data(filepath2)
    diff = make_diff(file1, file2)
    diff = formatted(format, diff)
    return diff
