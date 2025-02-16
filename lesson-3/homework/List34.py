original_list = [1, 2, 3, 4, 5]
n=int(input())
rotated_list = original_list[-n:] + original_list[:-n]
print(rotated_list)
