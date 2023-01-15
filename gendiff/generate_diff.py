import json
import itertools


SIGN = ['  +', '  -', '   ']


def choosing_sign(file, key, sign):
    value = file[key]
    return f'{sign} {key}: {value}'


def generate_diff(filepath1, filepath2):
    l = []
    file1 = json.load(open(filepath1))
    file2 = json.load(open(filepath2))
    not_keys1 = file2.keys() - file1.keys()
    not_keys2 = file1.keys() - file2.keys()
    for key in not_keys1:
        l.append(choosing_sign(file2, key, SIGN[0] ))
    for key in not_keys2:
        l.append(choosing_sign(file1, key, SIGN[1]))
    file1_and_file2 = file1.keys() & file2.keys()
    for key in file1_and_file2:
        if file1[key] == file2[key]:
            l.append(choosing_sign(file1, key, SIGN[2]))
        else:
            l.append(choosing_sign(file1, key, SIGN[0]))
            l.append(choosing_sign(file2, key, SIGN[1]))
    result = '\n'.join(itertools.chain('{', l, '}'))
    return result
