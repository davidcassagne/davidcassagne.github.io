import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 2*np.pi, 30)
y = np.cos(x)
plt.plot(x, y, label="cos(x)")
plt.legend()

plt.show()
