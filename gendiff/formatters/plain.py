def format_value(data):
    if isinstance(data, bool):
        return f"{str(data).lower()}"
    elif isinstance(data, type(None)):
        return "null"
    elif isinstance(data, int):
        return data
    elif isinstance(data, (dict, list, tuple)):
        return "[complex value]"
    return f"'{data}'"


def format_plain(diff, route=''):
    result = []
    for dictionary in diff:
        status = dictionary['status']
        if len(route) > 1:
            key = route + '.' + dictionary['key']
        else:
            key = dictionary['key']
        if status == 'nested':
            result.append(format_plain(dictionary['value'], key))
        elif status == 'changed':
            old = format_value(dictionary['old'])
            new = format_value(dictionary['new'])
            result.append(
                f"Property '{key}' was updated. "
                f"From {old} to {new}")
        elif status == 'added':
            value = format_value(dictionary['value'])
            result.append(f"Property '{key}' was added with value: {value}")
        elif status == 'deleted':
            result.append(f"Property '{key}' was removed")
    result = '\n'.join(result)
    return result
