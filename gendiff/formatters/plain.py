def format_value(data):
    if isinstance(data, bool):
        return fstr(data).lower
    if isinstance(data, type(None)):
        return "null"
    if isinstance(data, (dict, list, tuple)):
        return "[complex value]"
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
            old = format(v['old'])
            new = format_value(v['new'])
            result.append(
                f"Property '{k}' was updated. From {old} to {new}\n")
        elif status == 'added':
            value = format_value(v['value'])
            result.append(
                    f"Property '{k}' was added with value: {value}\n")
        elif status == 'deleted':
            result.append(
                    f"Property '{k}' was removed\n")
    result = ''.join(result)
    return result
