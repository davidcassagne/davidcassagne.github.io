import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-8, 8, 201)
z = 5*np.exp(2j*x) + 7*np.exp(3j*x)

plt.plot(x, np.abs(z), label="module")
plt.plot(x, np.angle(z), label="argument")
plt.legend()

plt.show()

