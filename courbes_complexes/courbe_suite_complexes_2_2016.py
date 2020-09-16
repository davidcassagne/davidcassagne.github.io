import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 201)
z = 5*np.exp(2j*x) + 7*np.exp(3j*x)

X = np.array([x,x])

y0 = np.zeros(len(x))
y = np.abs(z)
Y = np.array([y0,y])

Z = np.array([z,z])
C = np.angle(Z)

plt.plot(x, y, "k")

plt.pcolormesh(X, Y, C, shading="gouraud", cmap=plt.cm.hsv, vmin=-np.pi, vmax=np.pi)
plt.colorbar()

plt.show()
