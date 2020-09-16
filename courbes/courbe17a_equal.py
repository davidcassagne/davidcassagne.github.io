import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 1, 0, 0])
y = np.array([0, 0, 1, 1, 0])
plt.plot(x, y)
plt.axis("equal")
plt.xlim(-1, 2)

plt.show()
