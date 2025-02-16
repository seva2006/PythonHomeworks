person={'name':"John",'age':30,'profession':"teacher"}
key=input()
if key in person:
    print(person[key])
else:
    print("key doesn't exist")