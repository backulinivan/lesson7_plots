import numpy as np
import matplotlib.pyplot as plt

def func(x):
    y1 = x**2+1
    y2 = 1 + np.tan(2/(3-np.cos(2*x)))
    y3 = np.exp(-abs(x)/10)
    y = np.log(y1, y2) * y3
    return(y)

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, func(x))
plt.xlabel(r'$x$')
plt.ylabel(r'$f(x)$')
plt.grid(True)
plt.show()
