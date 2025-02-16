list=[1,3,2,4,3,2,1,7,5]
element=int(input())
found=False
for i in range(len(list)):
    if list[i]==element:
        print(i)
        found=True

if not found:
    print("Element is not found")
