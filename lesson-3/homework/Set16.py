set={1,2,3,4,5,6,7,8,9,10}

for i in set.copy():
    if i%2!=0:
        set.remove(i)

print(set)