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

plt.subplot(411)
plt.plot(t,x)

# on effectue un ifftshift pour positionner le temps zero comme premier element
plt.subplot(412)
a = np.fft.ifftshift(x)
plt.plot(a)

A = np.fft.fft(a)
# on effectue un fftshift pour positionner la frequence zero au centre
X = dt*np.fft.fftshift(A)

# calcul des frequences avec fftfreq
n = t.size
freq = np.fft.fftfreq(n, d=dt)
f = np.fft.fftshift(freq)

# comparaison avec la solution exacte
plt.subplot(413)
plt.plot(f, np.real(X), label="fft")
plt.plot(f, np.sqrt(np.pi/alpha) * np.exp( -(np.pi*f)**2 / alpha), label="exact")
plt.legend()

plt.subplot(414)
plt.plot(f, np.imag(X))

plt.show()