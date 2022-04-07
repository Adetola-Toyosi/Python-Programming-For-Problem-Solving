import matplotlib.pyplot as plt

fig, axes = plt.subplots(1,2)

x = range(0,10,1)

axes[0].plot(x)
axes[0].set_xlabel('X')
axes[0].set_xlim(2, 8)
axes[0].set_ylabel('Y')
axes[0].set_ylim(4, 16)

plt.tight_layout()
plt.show()