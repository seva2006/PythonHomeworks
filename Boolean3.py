num=float(input())
if bool(num>0 and num%2==0 ):
    print("{} is positive and even".format(num))
elif num>0 and num%2!=0:
    print("{} is positive but not even".format(num))
elif num<0 and num%2==0:
    print("{} is not positive and even".format(num))
else:
    print("{} is not positive and not even".format(num))
