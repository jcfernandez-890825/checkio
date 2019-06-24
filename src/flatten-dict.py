def flatten(dictionary):
    # Iterator for looping over all the dictionary keys
    items = iter(dictionary.items())
    # A list with all nested dictionaries pending to be checked
    iter_lst = [items]
    # A list with the flatten keys
    flatten_key_lst = []
    # This will contain the whole flatten dictionary
    flatten_dct = {}

    # We loop as long there is nested dictionaries pending to be checked
    while iter_lst:
        # We get the key, value tuple on the current dictionary
        key, value = next(items, (None, None))

        # In case we exhausted the iterator
        if value is None:
            # We get the next dictionary iterator
            items = iter_lst.pop()
            # We remove one level of the flatten keys
            if flatten_key_lst:
                flatten_key_lst.pop()
            # And we continue flattening the dictionary keys
            continue

        # We add the new key to the list of flatten keys
        flatten_key_lst.append(key)
        # Either we found another level in the nested dictionaries
        if isinstance(value, dict) and value:
            # We add the current iterator to the nested dictionaries pending to be checked
            iter_lst.append(items)
            # And we go the the next level of nested dictionaries
            items = iter(value.items())
        # Or we reach the end
        else:
            # Since we have all the keys for this branch we add it to the flatten dictionary
            flatten_dct['/'.join(flatten_key_lst)] = value if value else ''
            # And we pop out the last key since we are moving one level up on the branch
            flatten_key_lst.pop()

    return flatten_dct


if __name__ == '__main__':
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten(
        {
            "name": {
                "first": "One",
                "last": "Drone"
            },
            "job": "scout",
            "recent": {},
            "additional": {
                "place": {
                    "zone": "1",
                    "cell": "2"
                }
            }
        }
    ) == {
        "name/first": "One",
        "name/last": "Drone",
        "job": "scout",
        "recent": "",
        "additional/place/zone": "1",
        "additional/place/cell": "2"
    }
    print('You all set. Click "Check" now!')
