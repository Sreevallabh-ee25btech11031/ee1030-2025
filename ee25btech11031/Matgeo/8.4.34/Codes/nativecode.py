import numpy as np
import matplotlib.pyplot as plt
import math

y = np.linspace(-8, 8, 1000)

x = (y*y)/4

plt.plot(x, y, label = "$y^2 = 4x$")

x_p = (3*0 + x)/(3+1)
y_p = (3*0 + y)/(3+1)

plt.plot([0,1], [0,2])
plt.scatter([0,1,0.25], [0,2,0.5])

plt.plot(x_p, y_p, label = "$y^2 = x$")

ax = plt.gca()
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['left'].set_position('zero')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='best')
plt.grid(False)
plt.axis('equal')
plt.xlim(-2, 2)
plt.ylim(-4, 4)


plt.savefig("../Figs/plot(py).png")
plt.show()

