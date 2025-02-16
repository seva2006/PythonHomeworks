list=[1,45,12,30,10,21,87,-25,31]
index=len(list)//2
if len(list)%2==0:
    print("Middle elements are: {} {}".format(list[index-1],list[index]))
else:
    print("Middle element is {}".format(list[index]))