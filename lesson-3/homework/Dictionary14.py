person = {'name': 'John', 'age': 30, 'profession': 'teacher','nickname':'John'}
input_value=input()
list1=[]
for key,value in person.items():
    if value==input_value:
        list1.append(key)

print(list1)



