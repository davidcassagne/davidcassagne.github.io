import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 51)
y = np.linspace(-2, 2, 41)
X, Y = np.meshgrid(x, y)

Z = (1 - X/2 + X**5 + Y**3) * np.exp(-X**2 - Y**2) # calcul du tableau des valeurs de Z

plt.pcolor(X, Y, Z, cmap=plt.cm.hot)
plt.colorbar()

plt.show()
