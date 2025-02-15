Input=str(input("Enter a string:"))
Input1=Input.split()
if bool(Input1[0]==Input1[-1]):
    print("Input string starts and ends with the same word")
else:
    print("Starts with: {}".format(Input1[0]))
    print("Ends with: {}".format(Input1[-1]))

