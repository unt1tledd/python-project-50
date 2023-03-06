STATUS = {'unchanged': ' ', 'added': '+', 'deleted': '-'}


def format_value(data, depth=1):
    result = ["{"]
    if not isinstance(data, dict):
        return data
    for k, v in data.items():
        result.append(f"\n{'  ' * depth} {k}: {format_value(v, depth + 2)}")
    result.append(f"\n{'  ' * (depth - 1)}}}")
    return ''.join(result)


def stylish_format(diff, depth=1):
    result = []
    for d in diff:
        status = d['status']
        if status == 'nested':
            result.append(f"{'   ' * depth}{d['key']}: {{\n"
                          f"{stylish_format(d['value'], depth + 2)}")
            result.append(f"{'  ' * (depth + 1)}}}\n")
        elif status == 'changed':
            result.append(f"{'  ' * depth}- {d['key']}: "
                          f"{format_value(d['old'], depth + 2)}\n")
            result.append(f"{'  ' * depth}+ {d['key']}: "
                          f"{format_value(d['new'], depth + 2)}\n")
        else:
            result.append(f"{'  ' * depth}{STATUS[status]} {d['key']}: "
                          f"{format_value(d['value'], depth + 2)}\n")
    result = ''.join(result)
    return result
