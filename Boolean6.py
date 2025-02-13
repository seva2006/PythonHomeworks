num=float(input())
if bool(num%3==0 and num%5==0):
    print("{} is divisible by 3 and 5".format(num))
elif num%3==0 and num%5!=0:
    print("{} is divisible by 3 but not by 5".format(num))
elif num%3!=0 and num%5==0:
    print("{} is divisible by 5 but not by 3".format(num))
else:
    print("{} is not divisible by 3 and 5".format(num))