str1 = input()
str2 = input()

if len(str1) == len(str2):
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print(f"{str1} and {str2} are not equal")
            break
    else:
        print(f"{str1} and {str2} are equal")
else:
    print(f"{str1} and {str2} are not equal")
