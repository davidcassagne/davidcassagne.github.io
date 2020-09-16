import numpy as np
import matplotlib.pyplot as plt

n = 20

# definition de a
a = np.zeros(n)
a[2] = 1

# visualisation de a
# on ajoute a droite la valeur de gauche pour la periodicite
plt.subplot(211)
plt.plot( np.append(a, a[0]) )

# calcul de k
k = np.arange(n)

# calcul de A
A = np.fft.fft(a)

# visualisation de A - Attention au changement de variable
# on ajoute a droite la valeur de gauche pour la periodicite
plt.subplot(212)
x = np.append(k, k[-1]+k[1]-k[0]) # calcul d'une valeur supplementaire
z = np.append(A, A[0])
X = np.array([x,x])

y0 = np.zeros(len(x))
y = np.abs(z)
Y = np.array([y0,y])

Z = np.array([z,z])
C = np.angle(Z)

plt.plot(x,y,'k')

plt.pcolormesh(X, Y, C, shading="gouraud", cmap=plt.cm.hsv, vmin=-np.pi, vmax=np.pi)
plt.colorbar()

plt.show()
