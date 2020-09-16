import numpy as np
import matplotlib.pyplot as plt

n = 20

# definition de a
m = np.arange(n)
a = np.cos(m * 2*np.pi/n)

# visualisation de a
plt.subplot(211)
plt.plot(a)

# calcul de A
A = np.fft.fft(a)

# visualisation de A
plt.subplot(212)
plt.plot(np.real(A))
plt.ylabel("partie reelle")

plt.show()
