STATUS = {'unchanged': ' ', 'added': '+', 'deleted': '-'}


def converse(data):
    correct_values = {None: 'null', True: 'true', False: 'false'}
    if isinstance(data, (bool, type(None))):
        data = correct_values[data]
    return data


def format_value(data, depth=1):
    result = ["{"]
    if not isinstance(data, (dict, list)):
        return converse(data)
    elif isinstance(data, dict):
        for key, val in data.items():
            val = converse(val)
            result.append(f" {'  ' * depth} {key}: {format_value(val, depth + 2)}")
        result.append(f"{'  ' * (depth - 1)}}}")
    return '\n'.join(result)


def format_stylish(diff, depth=1):
    result = []
    for dictionary in diff:
        status = dictionary['status']
        key = dictionary['key']
        if status == 'nested':
            result.append(f"{'  ' * depth}  {key}: {{\n"
                          f"{format_stylish(dictionary['value'], depth + 2)}")
            result.append(f"{'  ' * (depth + 1)}}}\n")
        elif status == 'changed':
            result.append(f"{'  ' * depth}- {key}: "
                          f"{format_value(dictionary['old'], depth + 2)}\n")
            result.append(f"{'  ' * depth}+ {key}: "
                          f"{format_value(dictionary['new'], depth + 2)}\n")
        else:
            result.append(f"{'  ' * depth}{STATUS[status]} {key}: "
                          f"{format_value(dictionary['value'], depth + 2)}\n")
    result = ''.join(result)
    return result
