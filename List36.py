list=[3,5,-7,-5,54,34,-76,12,17]
sum=0
for i in range(len(list)):
    if list[i]>0:
        sum+=list[i]


print("Sum of all positive elements in a list is {}".format(sum))