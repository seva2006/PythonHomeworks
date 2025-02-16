tuple1=(1,2,1,2,4,5,3,4,5,6)
temp_list=list(tuple1)
unique_list=[]
for i in temp_list:
    if i not in unique_list:
        unique_list.append(i)

unique_tuple=tuple(unique_list)
print(unique_tuple)
