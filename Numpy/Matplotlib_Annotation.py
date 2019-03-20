#annotation

import numpy as np
import matplotlib.pyplot as plt

X = np.linspace(-6, 6, 1024)
Y = np.sinc(X)
plt.title('A simple marker exercis')
plt.xlabel('array variables')
plt.ylabel('random variables')
plt.text(-5, 0.4, 'Matplotlib')
plt.plot(X, Y, color = 'r', marker = 'o', markersize = 9, markevery = 30, markerfacecolor = 'w', linewidth = 3.0,
         markeredgecolor = 'b')
plt.show()


def pq(I, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (I - mu) ** 2)

I =np.linspace(-6,6, 1024)
plt.plot(I, pq(I, 0., 1.), color = 'k', linestyle = 'solid')
plt.plot(I, pq(I, 0., .5), color = 'k', linestyle = 'dashed')
plt.plot(I, pq(I, 0., .25), color = 'k', linestyle = 'dashdot')

design = {
    'facecolor':'y',
    'edgecolor':'g',
    'boxstyle':'round'
}
plt.text(-4, 1.5, s ='Matplot Lib', bbox = design)
plt.plot(X,Y,c='k')
plt.show()


X = np.linspace(-4, 4, 1024)
Y = .25 * (X + 4.) * (X + 1.) * (X - 2.)
plt.annotate('Big Data', ha = 'center', va = 'bottom', xytext = (-1.5, 3.0), xy = (0.75, -2.7),
arrowprops = {'facecolor':'green', 'shrink':0.05, 'edgecolor':'black'})
plt.plot(X, Y)
plt.show()