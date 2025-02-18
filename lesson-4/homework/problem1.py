list1 = [1, 1, 2]
list2 = [2, 3, 4]
uncommon = []
for element in list1:
    if element not in list2:
        uncommon.append(element)
for element in list2:
    if element not in list1:
        uncommon.append(element)
print(uncommon)