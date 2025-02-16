person = {'name': 'John', 'age': 30, 'profession': 'teacher', 'city': 'New York', 'friend': 'John'}
value_to_count = input()
count = sum(1 for value in person.values() if value == value_to_count)
print(f"The value '{value_to_count}' appears {count} time(s) in the dictionary.")