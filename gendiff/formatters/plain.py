def format_value(data):
    if isinstance(data, bool):
        return f"'{str(data).lower()}'"
    elif isinstance(data, type(None)):
        return "'null'"
    elif isinstance(data, (dict, list, tuple)):
        return "[complex value]"
    return f"'{data}'"


def plain_format(diff, route=''):
    result = []
    for dictionary in diff:
        status = dictionary['status']
        if len(route) > 1:
            key = route + '.' + dictionary['key']
        else:
            key = dictionary['key']
        if status == 'nested':
            result.extend(plain_format(dictionary['value'], key))
        elif status == 'changed':
            old = format_value(dictionary['old'])
            new = format_value(dictionary['new'])
            result.append(
                f"Property '{key}' was updated. "
                f"From {old} to {new}\n")
        elif status == 'added':
            value = format_value(dictionary['value'])
            result.append(f"Property '{key}' was added with value: {value}\n")
        elif status == 'deleted':
            result.append(f"Property '{key}' was removed\n")
    result = ''.join(result)
    return result
