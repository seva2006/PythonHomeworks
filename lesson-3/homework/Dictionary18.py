from collections import defaultdict
default_dict = defaultdict(lambda: 0)
default_dict['name'] = 'John'
default_dict['age'] = 30
print(default_dict['profession'])
print(dict(default_dict))