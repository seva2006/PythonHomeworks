tuple=(1,2,3,4,5,6,7)
sorted_tuple = sorted(tuple, reverse=True)
second_smallest = sorted_tuple[len(tuple)-2]

print("Second smallest element:", second_smallest)