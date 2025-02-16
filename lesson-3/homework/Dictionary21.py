person = {'name': 'John', 'age': 30, 'profession': 'teacher','city':'New York'}
sorted_by_value = dict(sorted(person.items(), key=lambda item: str(item[1])))
print(sorted_by_value)