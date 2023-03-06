def make_diff(old_dict, new_dict):
    result = []
    all_key = old_dict.keys() | new_dict.keys()
    for key in sorted(all_key):
        if key in old_dict and key not in new_dict:
            result.extend({'status': 'deleted',
                           'key': key, 'value': old_dict[key]})
        elif key in new_dict and key not in old_dict:
            result.append({'status': 'added',
                           'key': key, 'value': new_dict[key]})
        elif key in new_dict and key in old_dict:
            old = old_dict[key]
            new = new_dict[key]
            if isinstance(old, dict) and isinstance(new, dict):
                result.append({'status': 'nested', 'key': key,
                               'value': make_diff(old, new)})
            elif old == new:
                result.append({'status': 'unchanged', 'key': key, 'value': old})
            else:
                result.append({'status': 'changed',
                               'key': key, 'old': old, 'new': new})
    return result
