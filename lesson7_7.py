import matplotlib.pyplot as plt
import math as m

a,b=float(input()),float(input())
_x=[x/100 for x in range(-1000,1000)]
y=[sum([b**n*m.cos(a**n*m.pi*x) for n in range(100)]) for x in _x]

plt.plot(_x,y)
plt.show()
