person = {'name': 'John', 'age': 30, 'profession': 'teacher'}
inverted_dict={}
for key,value in person.items():
    inverted_dict[value]=key

print(inverted_dict)