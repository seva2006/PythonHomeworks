list=[1,2,3,4,5]
number=int(input())
new_list=[]
for i in range(len(list)):
    new_list.extend([list[i]]*number)

print(new_list)