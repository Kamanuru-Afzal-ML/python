def Divide_with_zero(num):
    return num/1
try:
    x=0
    Divide_with_zero(100)
    print(x)
except ZeroDivisionError:
    print("Do not divide number with zero")
except  SyntaxError:
    print("there is a syntax error")
else:
    print("No errors found")
finally:
    print("done")

try:
    print(x)
    x=0+'1'
except TypeError:
    print("Type error")
except Exception as err:
    print("error: %s" % err)

try:
    y=-1
    if(y<0):
        raise ValueError("value must be positive")
except ValueError as err:
    print(err)



