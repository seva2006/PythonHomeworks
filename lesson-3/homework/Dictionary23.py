dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'd': 5, 'e': 6}
common_keys = set(dict1.keys()) & set(dict2.keys())
if common_keys:
    print(f"Common keys: {common_keys}")
else:
    print("No common keys")
