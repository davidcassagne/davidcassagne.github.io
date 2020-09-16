import numpy as np
import matplotlib.pyplot as plt

alpha = 10

nc = 40
dt = 0.1
tmax = (nc-1) * dt
tmin = -nc * dt

# definition d'un signal gaussien
t = np.linspace(tmin, tmax, 2*nc)
x = np.exp(-alpha * t**2)

plt.subplot(211)
plt.plot(t,x)

# on effectue un ifftshift pour positionner le temps zero comme premier element
a = np.fft.ifftshift(x)

A = np.fft.fft(a)
# on effectue un fftshift pour positionner la frequence zero au centre
X = dt*np.fft.fftshift(A)

# calcul des frequences avec fftfreq
n = t.size
freq = np.fft.fftfreq(n, d=dt)
f = np.fft.fftshift(freq)

# visualisation de X - Attention au changement de variable
# on ajoute a droite la valeur de gauche pour la periodicite
plt.subplot(212)
x = np.append(f, f[0]) # calcul d'une valeur supplementaire
z = np.append(X, X[0])
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
