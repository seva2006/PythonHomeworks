tuple1=(1,2,3,4)
number=int(input())
temp_list=list(tuple1)
new_list=[]
for i in range(len(temp_list)):
    new_list.extend([temp_list[i]]*number)

new_tuple=tuple(new_list)
print(new_tuple)