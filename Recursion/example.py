def addMe(x):
    print(x)
    x+=1
    if x>20:
        return x
    addMe(x)
addMe(10)