tuple1=(1,2,3,4,5,6)
length_of_subtuple=int(input())
temp_list=list(tuple1)
nested_list=[]
for i in range(0,len(temp_list),length_of_subtuple):
    sublist=tuple(temp_list[i:i+length_of_subtuple])
    nested_list.append(sublist)

nested_tuple=tuple(nested_list)
print(nested_tuple)