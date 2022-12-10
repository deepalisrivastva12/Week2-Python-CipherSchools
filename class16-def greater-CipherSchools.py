def greater(a,b,c):
    if a>b and a>c:
        return b
    elif b>a and b>c:
        return b
    else:
        return c
print(greater(20,30,10))
#another method to find the greatest number 
def greatest(a,b,c):
    bigger=greater(a,b)
    return (bigger,c)
print(greater(1100,500,7497))