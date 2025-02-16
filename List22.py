list=[1,2,3,4,5,6,7,8,9,10]
new_list=[]
for i in list:
    if i%2==0:
        new_list.append(i)

print("New list with even numbers: {}".format(new_list))
