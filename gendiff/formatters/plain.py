def format_value(data):
    if isinstance(data, bool):
        return f"'{data.lower}'"
    elif isinstance(data, (dict, list, tuple)):
        return "[complex value]"
    elif isinstance(data, type(None)):
        return "null"
    return f"'{data}'"


def plain_format(diff, route=''):
    result = []
    for d in diff:
        status = d['status']
        if len(route) > 1:
            k = route + '.' + d['key']
        if status == 'nested':
            result.extend(plain_format(d['value'], k))
        elif status == 'changed':
            old = format_value(d['old'])
            new = format_value(d['new'])
            result.append(
                f"Property '{k}' was updated. "
                f"From {old} to {new}\n")
        elif status == 'added':
            value = format_value(d['value'])
            result.append(
                    f"Property '{k}' was added with value: {value}\n")
        elif status == 'deleted':
            result.append(
                    f"Property '{k}' was removed\n")
    result = ''.join(result)
    return result
