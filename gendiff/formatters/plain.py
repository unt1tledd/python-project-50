def format_value(data):
    if isinstance(data, bool):
        return fstr(data).lower
    elif isinstance(data, (dict, list, tuple)):
        return "[complex value]"
    elif isinstance(data, type(None)):
        return "null"
    else:
        data = str(data)
    return f"'{data}'"


def plain_format(diff, route = ''):
    result = []
    for k, v in sorted(diff.items()):
        status = v['status']
        if len(route) > 1:
            k = route + '.' + k
        if status == 'nested':
            result.extend(plain_format(v['value'], k))
        elif status == 'changed':
            old = format_value(v['old'])
            new = format_value(v['new'])
            result.append(
                f"Property '{k}' was updated. "
                f"From {format_value(old)} to {format_value(new)}\n")
        elif status == 'added':
            value = format_value(v['value'])
            result.append(
                    f"Property '{k}' was added with value: {value}\n")
        elif status == 'deleted':
            result.append(
                    f"Property '{k}' was removed\n")
    result = ''.join(result)
    return result
