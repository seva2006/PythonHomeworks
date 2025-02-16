tuple=(1,1,2,3,4,3,5,6,7,2,3,4,6,7)
element=int(input())
found=False
for i in range(len(tuple)):
    if tuple[i]==element:
        print(i)
        found=True

if not found:
    print("Element not found")

