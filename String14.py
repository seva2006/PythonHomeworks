str1=str(input())
str2=str(input())
if len(str1)==len(str2):
    for i in range(0,len(str1)-1):
        if str1[i]==str2[i]:
            i=i+1
        else:
            print(f"{str1} and {str2} are not equal")

            print(f"{str1} and {str2} are equal")

else:
    print(f"{str1} and {str2} are not equal")
