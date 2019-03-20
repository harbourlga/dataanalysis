# import matplotlib.pyplot as plt



#1
class huatu():
    def __init__(self):
        pass
    def plot_huatu(self, x, y):
        import matplotlib.pyplot as plt
        plt.plot(x, y)
        plt.show()


import numpy as np
#1
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
huatu().plot_huatu(x, y)

#2
x = np.linspace(-3, 2, 200)
Y = x**2-2*x+1
huatu().plot_huatu(x, Y)

#3
import matplotlib.pyplot as plt
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
z = np.cos(x)
plt.plot(x, y)
plt.plot(x, z)
plt.show()

#4
data = np.loadtxt(r'numpy.txt')
print(data)
plt.plot(data[:,0], data[:,1])
plt.show()


#5
data_1 = np.loadtxt(r'scipy.txt')
print(data_1.T)
for val in data_1.T:
    plt.plot(data_1[:,0], val)


plt.show()


##Scatter Plots and Bar Graphs


#6
sct = np.random.rand(20, 2)
print(sct)
plt.scatter(sct[:,0], sct[:,1])
plt.show()


#7
ghj = [5, 10, 15, 20, 25]
it = [1, 2, 3, 4, 5]
plt.bar(ghj, it, width = 5)
plt.show()


#8
ghj = ['a', 'b', 'c', 'd', 'e']
plt.barh(ghj, it)
plt.show()


#Multiple bar charts
#9
new_list = [[41, 52, 33, 43], [51, 63, 72, 51], [33, 43, 22, 50]]
x = np.arange(4)
plt.bar(x + 0.00, new_list[0], color = 'b', width = 0.25)
plt.bar(x + 0.25, new_list[1], color = 'r', width = 0.25)
plt.bar(x + 0.50, new_list[2], color = 'g', width = 0.25)
plt.show()

#10
p = [5., 30., 45., 22.]
q = [5., 25., 50., 20.]
x = range(4)
plt.bar(x, p, color='b')
plt.bar(x, q, color='y', bottom =p)
plt.show()

#11
plt.bar(x, q, color='y')
plt.bar(x, p, color='b', bottom =q)
plt.show()

#12
A = np.array([5., 30., 45., 22.])
B = np.array([5., 25., 50., 20.])
C = np.array([1., 2., 1., 1.])
X = np.arange(4)
plt.bar(X, A, color = 'b')
plt.bar(X, B, color = 'g', bottom = A)
plt.bar(X, C, color = 'r', bottom = A+B)
plt.show()


#13
black_money = np.array([5., 30., 45., 22.])
white_money = np.array([5., 25., 50., 20.])
z = np.arange(4)
plt.barh(z, black_money, color = 'g')
plt.barh(z, -white_money, color = 'r')
plt.show()




# Other Plots
#14
y = [5, 25, 45, 65]
plt.pie(y)
plt.show()

#15
d = np.random.randn(100)
plt.hist(d, bins = 20)
plt.show()

#16
d = np.random.randn(100)
plt.boxplot(d)
plt.show()

#2nd 部分:
#17
p = np.random.standard_normal((50, 2))
print('p:{}'.format(p))
p += np.array((-1, 1))
print('p_change:{}'.format(p))
q = np.random.standard_normal((50, 2))
q += np.array((1, 1))
plt.scatter(p[:,0], p[:,1], color = '.25')
plt.scatter(q[:,0], q[:,1], color = '.75')
plt.show()



#18
dd = np.random.standard_normal((50, 2))
plt.scatter(dd[:,0], dd[:,1], color = '1.0', edgecolor = '0.0')
plt.show()

#19
vals = np.random.random_integers(99, size = 50)
color_set = ['.00','.25','.50','.75']
color_lists = [color_set[(len(color_set)* val)//100] for val in vals]
c = plt.bar(np.arange(50), vals, color = color_lists)
plt.show()


#20
hi = np.random.random_integers(8, size=10)
color_set = ['.00','.25','.50','.75']
plt.pie(hi, colors = color_set)
plt.show()