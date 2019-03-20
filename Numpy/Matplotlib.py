import matplotlib.pyplot as plt
import numpy as np

x =  np.arange(100)
y =[val**2 for val in x]
plt.plot(x,y)
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2)
for ax in axes:
    ax.plot(x, y, 'r')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('title')

fig.tight_layout()
plt.show()

fig, ax = plt.subplots()
plt.axis([0,5,0,100])
ax.plot(x, x**2, label="y = x**2")
ax.plot(x, x**3, label="y = x**3")
ax.legend(loc=2); #upper left corner
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('title')

fig.tight_layout()
plt.show()

fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(10, 4))
axes[0].axis([0,5,0,160])
axes[0].plot(x, x**2, x, np.exp(x))
axes[0].set_title("Normal scale")
axes[1].axis([0,5,0.1,1000])
axes[1].plot(x, x**3, x, np.exp(x))
axes[1].set_yscale("log")
axes[1].set_title("Logarithmic scale(y)")
plt.show()


n = np.array([0, 1, 2, 3, 4, 5])
xx = np.random.rand(100)
fig, axes = plt.subplots(1, 4, figsize=(12, 3))
axes[0].axis([0,1,-1.5,1.5])
axes[0].scatter(xx, xx + 0.25*np.random.randn(len(xx)))
axes[0].set_title("scatter")
axes[1].axis([0, 5, 0, 25])
axes[1].step(n, n**2, lw=2)
axes[1].set_title("step")
axes[2].axis([-1, 6, 0, 25])
axes[2].bar(n, n**2, align="center", width = 0.5, alpha=0.5)
axes[2].set_title("bar")
axes[3].axis([0, 5, 0, 140])
axes[3].fill_between(x, x**2, x**3, color="green", alpha=0.5)
axes[3].set_title("fill_between")
plt.show()



