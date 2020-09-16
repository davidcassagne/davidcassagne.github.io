import numpy as np
import matplotlib.pyplot as plt

nbx = 101
x = np.linspace(0, 10, nbx)
y = np.cos(x)

# préparation des tableaux qui vont recevoir les valeurs
xnew = np.zeros(nbx-1)
yp = np.zeros(nbx-1)

# calcul des abscisses et des valeurs de la dérivée
for i in range(nbx-1): 
    xnew[i] = (x[i] + x[i+1]) / 2
    yp[i] = (y[i+1] - y[i]) / (x[i+1] - x[i])
    
plt.plot(x, y, label="f(x)")
plt.plot(xnew, yp, label="f'(x)")

plt.legend()
plt.show() 
