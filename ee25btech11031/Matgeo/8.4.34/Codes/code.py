import numpy as np
import matplotlib.pyplot as plt
import ctypes

c_lib=ctypes.CDLL("./code.so")

c_lib.compute_parabola.argtypes = [
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.c_int
]

y = np.linspace(-5,5,100)
x = np.zeros_like(y)

c_lib.compute_parabola(
    y.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    x.ctypes.data_as(ctypes.POINTER(ctypes.c_double)),
    y.size
)

plt.plot(x, y, color = 'red' ,label = "$y^2 = 4x$")

x_p = (3*0 + x)/(3+1)
y_p = (3*0 + y)/(3+1)

plt.plot([0,1], [0,2], color = 'black')
plt.scatter([0,1,0.25], [0,2,0.5])

plt.plot(x_p, y_p, color = 'green', label = "$y^2 = x$")

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


plt.savefig("../Figs/plot(py+C).png")
plt.show()

