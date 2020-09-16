import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 51)
y = np.linspace(-3, 3, 51)
X, Y = np.meshgrid(x, y)

C = np.angle(X + 1j *Y) 

plt.pcolormesh(X, Y, C, shading="gouraud")
plt.colorbar()
plt.xlabel("partie reelle")
plt.ylabel("partie imaginaire")

plt.show()
