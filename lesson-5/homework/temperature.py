def convert_cel_to_far():
    F=C*9/5+32
    return F

def convert_far_to_cel():
    C=(F-32)*5/9
    return C
C=float(input("Enter a temperature in degrees C:"))
F = float(input("Enter a temperature in degrees F:"))
Celsius=convert_far_to_cel()
Fahrenheit=convert_cel_to_far()
print("{} degrees F = {} degrees C".format(int(F),round(Celsius,2)))
print("{} degrees C = {} degrees F".format(int(C),round(Fahrenheit,2)))

