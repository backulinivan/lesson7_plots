import numpy as np
import matplotlib.pyplot as plt

def func(x):
    return(x**2-6-x)

def rootSearch(a, b, f):
    eps = 0.0000001
    while abs(a - b) > eps:
        if f(a)*f((a+b)/2) < 0:
            b = (a+b)/2
        elif f(b)*f((a+b)/2) < 0:
            a = (a+b)/2
    return((a+b)/2)            

root1 = rootSearch(-5, 1/12, func)
root2 = rootSearch(1/12, 6, func)
print(root1, root2)            

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x**2-6-x)
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
