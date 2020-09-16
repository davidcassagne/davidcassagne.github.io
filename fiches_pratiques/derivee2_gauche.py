import numpy as np
import matplotlib.pyplot as plt

nbx = 101
x = np.linspace(0, 10, nbx)
y = np.cos(x)

# calcul des valeurs de la dérivée
yp = (y[1:] - y[:-1]) / (x[1:] - x[:-1])
    
plt.plot(x, y, label="f(x)")
plt.plot(x[:-1], yp, label="f'(x)")

plt.legend()
plt.show()
