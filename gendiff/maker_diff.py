def make_diff(old_dict, new_dict):
    result = {}
    deleted_keys = old_dict.keys() - new_dict.keys()
    for key in deleted_keys:
        result[key] = {'status': 'deleted', 'value': old_dict[key]}
    unchanged_keys = new_dict.keys() & old_dict.keys()
    added_keys = new_dict.keys() - old_dict.keys()
    for key in added_keys:
        result[key] = {'status': 'added', 'value': new_dict[key]}
    for key in sorted(unchanged_keys):
        old_value = old_dict[key]
        new_value = new_dict[key]
        if isinstance(old_value, dict) and isinstance(new_value, dict):
            result[key] = {'status': 'nested',
                           'value': make_diff(old_value, new_value)}
        elif old_value == new_value:
            result[key] = {'status': 'unchanged',
                           'value': new_value}
        elif old_value != new_value:
            result[key] = {'status': 'changed',
                           'old': old_value,
                           'new': new_value}
    return dict(sorted(result.items()))
