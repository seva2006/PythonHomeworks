person={'name':"John",'age':30,'profession':"teacher"}
key=input()
if key in person:
    person.pop(key)
else:
    print("key doesn't exist")

print(person )