list=[1,3,2,4,3,2,1,7,5]
unique_list=[]
for i in list:
    if i not in unique_list:
        unique_list.append(i)

print(unique_list)

