person = {'name': 'John', 'age': 30, 'profession': 'teacher'}
key=input()
new_value=input()
if key in person:
    person[key] = new_value
    print(f"Updated dictionary: {person}")
else:
    print("Key doesn't exist.")