str1=str(input())
str2=str(input())
if bool(len(str1)==len(str2)):
    print("{} and {} have the same length".format(str1,str2))
else:
    print("{} and {} have different length".format(str1,str2))