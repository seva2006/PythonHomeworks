import math

def is_prime(n):
    if n <= 1:
        print("{} is not prime".format(n))
        return
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            print("{} is not prime".format(n))
            return
    print("{} is prime".format(n))

n = int(input("Enter a number: "))
is_prime(n)


