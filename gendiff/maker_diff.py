def make_diff(old_dict, new_dict):
    result = []
    all_key = old_dict.keys() | new_dict.keys()
    for key in sorted(all_key):
        if key not in new_dict:
            result.append({'key': key, 'status': 'deleted',
                           'value': old_dict[key]})
        elif key not in old_dict:
            result.append({'key': key, 'status': 'added',
                           'value': new_dict[key]})
        elif key in new_dict and key in old_dict:
            old = old_dict[key]
            new = new_dict[key]
            if isinstance(old, dict) and isinstance(new, dict):
                result.append({'key': key, 'status': 'nested',
                               'value': make_diff(old, new)})
            elif old == new:
                result.append({'key': key, 'status': 'unchanged', 'value': old})
            else:
                result.append({'key': key, 'status': 'changed',
                               'old': old, 'new': new})
    return result
