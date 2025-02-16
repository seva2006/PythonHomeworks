person={'name':"John",'age':30,'profession':"teacher"}
key=input()
value = person.get(key)
if value is not None:
    print(f"The key-value pair is: {key}: {value}")
else:
    print("Key doesn't exist.")