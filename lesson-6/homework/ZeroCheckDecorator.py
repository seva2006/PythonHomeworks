def check(func):
    def wrapper(a,b):
        if b==0:
            print("Denominator can't be zero")
        else:
            return func(a,b)
    return wrapper

@check
def div(a, b):
   return a / b

print(div(10,0))