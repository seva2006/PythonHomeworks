def factors(number):
    if(number<0):
        print("Incorrect number")
    else:
        for i in range(1,number+1):
            if number%i==0:
                print("{} is a factor of {}".format(i,number))


number=int(input("Enter a positive integer:"))
factors(number)