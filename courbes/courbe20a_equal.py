import numpy as np
import matplotlib.pyplot as plt

theta = np.linspace(0, 2*np.pi, 40)

x = np.cos(theta)
y = np.sin(theta)
plt.plot(x, y)
plt.axis("equal")
plt.xlim(-3,3)

plt.show()
