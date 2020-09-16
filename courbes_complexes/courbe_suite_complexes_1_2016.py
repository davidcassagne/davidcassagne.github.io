import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 201)
z = 5*np.exp(2j*x) + 7*np.exp(3j*x)

plt.plot(x, np.real(z), label="real")
plt.plot(x, np.imag(z), label="imag")
plt.legend()

plt.show()
