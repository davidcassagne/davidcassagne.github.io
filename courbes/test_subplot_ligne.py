import matplotlib.pyplot as plt

plt.subplot(121)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, "subplot(121)", ha="center", va="center", size=24, alpha=.5)

plt.subplot(122)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, "subplot(122)", ha="center", va="center", size=24, alpha=.5)

plt.show()