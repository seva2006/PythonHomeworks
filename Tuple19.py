tuple1=(1,2,3,2,4,6,2,1,2,4)
element=int(input())
temp_list=list(tuple1)
if element in temp_list:
    temp_list.remove(element)

new_tuple=tuple(temp_list)
print(new_tuple)


