tuple=(1,2,3,4,5,6)
sorted=True
for i in range(len(tuple)-1):
    if tuple[i]>tuple[i+1]:
        sorted=False

if sorted:
    print("Sorted in ascending order")
else:
    print("Not sorted")


