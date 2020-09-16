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

plt.subplot(411)
plt.plot(x,f)

# on effectue un ifftshift pour positionner le temps zero comme premier element
plt.subplot(412)
a = np.fft.ifftshift(f)
plt.plot(a)

A = np.fft.fft(a)
# on effectue un fftshift pour positionner la frequence zero au centre
g = dx/np.sqrt(2*np.pi)*np.fft.fftshift(A)

# calcul des frequences avec fftfreq
n = x.size
freq = 2*np.pi * np.fft.fftfreq(n, d=dx)
k = np.fft.fftshift(freq)

# comparaison avec la solution exacte
plt.subplot(413)
plt.plot(k, np.real(g), label="fft")
plt.plot(k, 1/np.sqrt(alpha) * np.exp( -k**2 / (2*alpha)), label="exact")
plt.legend()

plt.subplot(414)
plt.plot(k, np.imag(g))

plt.show()