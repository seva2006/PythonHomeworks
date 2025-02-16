person = {'name': 'John', 'age': 30, 'profession': 'teacher','address':{'city':'New York','zipcode':'140253'}}
for key,value in person.items():
    if isinstance(value,dict):
        print(f"The value of the key '{key}' is a nested dictionary:", value)