from math import *

def func(x):
    y = -(sin(x)+1+log(1.25+x**(-15)))/log(1+x**2)
    return(y)
    
print(func(1), func(10), func(1000))    
