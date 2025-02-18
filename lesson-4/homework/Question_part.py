# 1. The main difference between continue and break statements is that continue skips the current iteration of the loop and
# moves to the next iteration, while break terminates the entire loop, regardless of the number of iterations remaining.
# 2. Well, usually for loop is used when we know the number of iterations. While loop is usually used when you don't
# know the number of iterations and you want to loop until the condition becomes false.
# 3.A nested for loop is a loop inside another loop. It’s typically used when we need to iterate over multi-dimensional
# data structures, such as a matrix, or when we need to perform operations that require multiple layers of
# iteration.
for i in range(1, 4):
    for j in range(i):
        print("*", end=" ")
    print()
