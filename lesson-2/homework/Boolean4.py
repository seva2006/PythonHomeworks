num1=float(input())
num2=float(input())
num3=float(input())
if bool(num1==num2 and num2==num3):
    print("{},{},{} are equal".format(num1,num2,num3))
elif num1==num2 and num2!=num3:
    print("{},{} are equal, but not {}".format(num1,num2,num3))
elif num1==num3 and num2!=num3:
    print("{},{} are equal, but not {}".format(num1,num3,num2))
else:
    print("{},{},{} are all different".format(num1,num2,num3))