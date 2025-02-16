list=[8,7,56,4,5,3,47,23,43,1,-6,-4,-9]
count=0
for i in list:
    if i%2!=0:
        count+=1
    else:
        continue

print(count)