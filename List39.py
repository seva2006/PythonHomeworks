list=[1,2,3,4,5,6,7,8,9]
length_of_sublist=int(input())
nested_list=[]
for i in range(0,len(list),length_of_sublist):
    sublist=list[i:i+length_of_sublist]
    nested_list.append(sublist)

print(nested_list)