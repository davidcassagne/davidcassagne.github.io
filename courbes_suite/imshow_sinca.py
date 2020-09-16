import numpy as np
import matplotlib.pyplot as plt

epsilon = np.finfo(float).eps
print("epsilon =", epsilon)

xmin = -8
xmax = 8
nbx = 41
ymin = -8
ymax = 8
nby = 41

x = np.linspace(xmin, xmax, nbx)
y = np.linspace(ymin, ymax, nby)
X, Y = np.meshgrid(x, y)

R = np.sqrt(X**2 + Y**2) + epsilon
Z = np.sin(R) / R

plt.imshow(Z, interpolation="bicubic", 
       origin="lower", extent=[xmin,xmax,ymin,ymax])
plt.colorbar()

plt.show()
