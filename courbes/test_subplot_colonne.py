import matplotlib.pyplot as plt

plt.subplot(211)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, "subplot(211)", ha="center", va="center", size=24, alpha=.5)

plt.subplot(212)
plt.xticks([])
plt.yticks([])
plt.text(0.5, 0.5, "subplot(212)", ha="center", va="center", size=24, alpha=.5)

plt.show()