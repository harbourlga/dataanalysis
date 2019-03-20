# how to color scatter plots
#Colormaps are defined in the matplotib.cm module.
# This module provides functions to create and use colormaps.
# It also provides an exhaustive choice of predefined color maps.

import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

N = 256
angle = np.linspace(0, 8*2*np.pi, num=N)
radius = np.linspace(.5, 1., N)
X = radius * np.cos(angle)+1
Y = radius * np.sin(angle)
plt.scatter(X, Y, c=angle, cmap = cm.hsv)
plt.show()


#Line Styles

# creating 3 levels of gray plots, with different line shades
def pq(I, mu, sigma):
    a = 1. / (sigma * np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma ** 2)
    return a * np.exp(b * (I-mu) ** 2)

I = np.linspace(-6 , 6, 1024)

plt.plot(I, pq(I, 0., 1.), color = 'k', linestyle = 'solid')
plt.plot(I, pq(I, 0., .5), color = 'k', linestyle = 'dashed')
plt.plot(I, pq(I, 0., .25), color = 'k', linestyle = 'dashdot')
plt.show()


#3
N = 15
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)
plt.bar(X, A, color = '.75')
plt.bar(X, A+B, bottom = A, color = 'w', linestyle = 'dashed',linewidth = .75)
plt.show()


#4
def gf(X, mu, sigma):
    a = 1. / (sigma*np.sqrt(2. * np.pi))
    b = -1. / (2. * sigma **2)
    return a * np.exp(b * (X-mu) ** 2)

X = np.linspace(-6, 6, 1024)
for i in range(64):
    samples = np.random.standard_normal(50)
    mu, sigma = np.mean(samples), np.std(samples)
    plt.plot(X, gf(X, mu, sigma), color = '.75', linewidth = .5)

plt.plot(X, gf(X, 0., 1.), color ='.00', linewidth = 3.)
plt.show()



#5
N = 15
A = np.random.random(N)
B = np.random.random(N)
X = np.arange(N)
plt.bar(X, A, color = 'w', hatch = 'x')
plt.bar(X, A+B, bottom = A, color = 'r', hatch ='/')
plt.show()


#6
X = np.linspace(-6, 6, 1024)
Ya = np.sinc(X)
Yb = np.sinc(X) + 1
plt.plot(X, Ya, marker = 'o', color = '.75')
plt.plot(X, Yb, marker = '^', color = '.00', markevery = 32)
plt.show()

#7
A = np.random.standard_normal((50, 2))
print('A:{}'.format(A))
A += np.array((-1, 1))
print('A:{}'.format(A))
B = np.random.standard_normal((50, 2))
B += np.array((1, 1))
plt.scatter(A[:,0], A[:,1], color = 'k', s = 25.0)
plt.scatter(B[:,0], A[:,1], color = 'g', s = 100.0) #s is 'size'
plt.show()


#8
X = np.linspace(-6, 6, 1024)
Y = np.sinc(X)
plt.plot(X, Y, color = 'r', marker = 'o', markersize = 9, markevery= 30, markerfacecolor = 'w', linewidth=3.0,markeredgecolor = 'b')
plt.show()

#9
import matplotlib as mpl
mpl.rc('lines', linewidth = 3)
mpl.rc('xtick', color = 'w')
mpl.rc('ytick', color = 'w')
mpl.rc('axes', facecolor = 'g', edgecolor = 'y')
mpl.rc('figure', facecolor = '.00', edgecolor = 'w')
# mpl.rc('axes', color_cycle = ('y', 'r'))
x = np.linspace(0, 7, 1024)
plt.plot(x, np.sin(x))
plt.plot(x, np.cos(x))
plt.show()