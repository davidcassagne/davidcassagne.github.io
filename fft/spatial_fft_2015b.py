import numpy as np
import matplotlib.pyplot as plt

alpha = 20

nc = 40
dx = 0.1
xmax = (nc-1) * dx
xmin = -nc * dx

# definition d'un signal gaussien
x = np.linspace(xmin, xmax, 2*nc)
f = np.exp(-alpha/2 * x**2)

plt.subplot(211)
plt.plot(x,f)

# on effectue un ifftshift pour positionner le temps zero comme premier element
a = np.fft.ifftshift(f)

A = np.fft.fft(a)
# on effectue un fftshift pour positionner la frequence zero au centre
g = dx/np.sqrt(2*np.pi)*np.fft.fftshift(A)

# calcul des frequences avec fftfreq
n = x.size
freq = 2*np.pi * np.fft.fftfreq(n, d=dx)
k = np.fft.fftshift(freq)

# visualisation de X - Attention au changement de variable
# on ajoute a droite la valeur de gauche pour la periodicite
plt.subplot(212)
x = np.append(k, k[0]) # calcul d'une valeur supplementaire
z = np.append(g, g[0])
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