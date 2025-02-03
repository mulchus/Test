def compare_templates_indexes(curent_templates_index: dict, new_templates_index: dict) -> tuple:
    curent_templates_index_keys = set(curent_templates_index.keys())
    new_templates_index_keys = set(new_templates_index.keys())
    shared_keys = curent_templates_index_keys.intersection(new_templates_index_keys)
    removed = {key: curent_templates_index[key] for key in (curent_templates_index_keys - new_templates_index_keys)}
    added = {key: new_templates_index[key] for key in (new_templates_index_keys - curent_templates_index_keys)}
    modified = ({o: (curent_templates_index[o], new_templates_index[o])
                for o in shared_keys if curent_templates_index[o] != new_templates_index[o]})
    same = set(o for o in shared_keys if curent_templates_index[o] == new_templates_index[o])
    return added, removed, modified, same


curent_templates_index = {'a': 1, 'd': 2, 'z': 3, 'p': 20}
new_templates_index = {'a': 12, 'c': 4, 'b': 5, 'p': 20}
# print(new_templates_index['b'])
removed, added, modified, same = compare_templates_indexes(curent_templates_index, new_templates_index)
print(added, removed, modified, same)

#
# delete_item = dict(dict1.items() - dict2.items())
# print(delete_item)
#
# new_item = dict(dict2.items() - dict1.items())
# print(new_item)
#
# changed_item = dict(delete_item.items() - new_item.items())
# print(changed_item)

