list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sublist = [3, 4, 5]
if any(list[i:i+len(sublist)] == sublist for i in range(len(list) - len(sublist) + 1)):
    print("Sublist exists in the list")
else:
    print("Sublist does not exist in the list")

