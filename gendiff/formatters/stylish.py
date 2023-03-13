from gendiff.cli import conversed


STATUS = {'unchanged': ' ', 'added': '+', 'deleted': '-'}


def format_value(data, depth=1):
    result = ["{"]
    if not isinstance(data, (dict, list)):
        return conversed(data)
    elif isinstance(data, dict):
        for key, value in data.items():
            value = conversed(value)
            result.append(f"\n{'  ' * depth} {key}: {format_value(value, depth + 2)}")
            result.append(f"\n{'  ' * (depth - 1)}}}")
    return ''.join(result)


def stylish_format(diff, depth=1):
    result = []
    for dictionary in diff:
        status = dictionary['status']
        if status == 'nested':
            result.append(f"{'   ' * depth}{dictionary['key']}: {{\n"
                          f"{stylish_format(dictionary['value'], depth + 2)}")
            result.append(f"{'  ' * (depth + 1)}}}\n")
        elif status == 'changed':
            result.append(f"{'  ' * depth} - {dictionary['key']}: "
                          f"{format_value(dictionary['old'], depth + 2)}\n")
            result.append(f"{'  ' * depth} + {dictionary['key']}: "
                          f"{format_value(dictionary['new'], depth + 2)}\n")
        else:
            result.append(f"{'  ' * depth} {STATUS[status]} {dictionary['key']}: "
                          f"{format_value(dictionary['value'], depth + 2)}\n")
    result = ''.join(result)
    return result
