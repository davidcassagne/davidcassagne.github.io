import numpy as np
import matplotlib.pyplot as plt

xmin = -3
xmax = 3
nbx = 51
ymin = -2
ymax = 2
nby = 41

x = np.linspace(xmin, xmax, nbx)
y = np.linspace(ymin, ymax, nby)
X, Y = np.meshgrid(x, y)

Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2) # calcul du tableau des valeurs de Z

plt.imshow(Z, interpolation="bicubic", 
           origin="lower", extent=[xmin,xmax,ymin,ymax])
plt.colorbar()

plt.show()
