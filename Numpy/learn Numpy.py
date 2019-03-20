#learn Numpy

import numpy as np


# scores = [89, 90.32, 91, 92]
# first_arr =np.array(scores)
# print(first_arr) #
# print(first_arr.dtype)


scores_1 = [[[34,22], [22,333], [22,44], [32,55]], [[22,66], [22,77], [44,77], [4,55]]]
second_arr = np.array(scores_1)
print(second_arr)
print(second_arr.ndim)
print(second_arr.shape)
print(second_arr.dtype)

x = np.zeros(10) #返回一维数组里面全是0
x_1 = np.zeros((4, 3))
print('x:', x , 'x_1:' , x_1)
print('x_1.dim:', x_1.ndim)

x_2 = np.arange(15)
print('np.arange(15):' , x_2)

x_3 = np.eye(6)
print('np.eye(6):', x_3)

scores = [89, 56.34, 76, 89, 98]
first_arr1 =np.array(scores)
print('first_arr1: ', first_arr1)
print(first_arr1*first_arr1)
print(first_arr1-first_arr1)
print(1/first_arr1)
print(first_arr1**0.05)
scores_1 = [[34,22,66], [22,333,77], [22,44,88]]
first_arr2 = np.array(scores_1)
print('first_arr2*first_arr2:{}'.format(first_arr2*first_arr2))

new_arr = np.arange(12)
print('new_arr:', new_arr)
print('new_arr[5]:', new_arr[5])
print('new_arr[4:9]:', new_arr[4:9])
new_arr[4:9] = 99
print(new_arr)
new_arr1 = np.arange(1, 12)
print('new_arr1:',new_arr1)
print('new_arr1[5]:{}'.format(new_arr1[5]))


modi_arr = new_arr[4:9]
print(modi_arr)
modi_arr[1] = 123456
print(new_arr)
print(modi_arr[:])
print(modi_arr)


matrix_arr = np.array([[3, 4, 5], [5, 4, 3], [2, 3, 3]])
print(matrix_arr)
print(matrix_arr[1])
print(matrix_arr[0][2])
print(matrix_arr[0,2])
three_d_arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print("three_d_arr's value{}".format(three_d_arr))
print(three_d_arr.ndim)
print("returns the second list inside first list: {}".format(three_d_arr[0, 1, 2]))
print(three_d_arr[0])
copied_values = three_d_arr[0].copy()
print("copied_values:{}".format(copied_values))
three_d_arr[0] = 99
print("New value of three_d_arr:{}".format(three_d_arr))
three_d_arr[0] = copied_values
print("three_d_arr again:{}".format(three_d_arr))


matrix_arr_1 = np.array([[3,3,2],[2,3,4],[5,4,5]])
print("The original matrix:{}".format(matrix_arr_1))
print("切割前面两行:{}".format(matrix_arr_1[:2]))
print("切割前面两行和后两列:{}".format(matrix_arr_1[:1,1:]))
print("返回第二行的前两列:{}".format(matrix_arr_1[1,:2]))
print("返回第三列:{}".format(matrix_arr_1[:,2:]))
print("返回第一和第三行:{}".format(matrix_arr_1[[0,2]]))


personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(personals == 'Manu')

from numpy import random
#生成随机数
random_no = random.randn(7, 4)
print("生成一组七行四列的随机数组:{}".format(random_no))
random_no_1 = random_no[personals == 'Manu']
print("切割第一和第四行:{}".format(random_no_1))
random_no_2 = random_no[personals == 'Manu', 2:]
print(" :{}".format(random_no_2))
print(personals != 'Manu')
random_no_3 = random_no[personals != 'Manu']
print("切割除第一和第四行:{}".format(random_no_3))
new_variable = (personals == 'Manu') | (personals == 'Jeevan')
print(new_variable)
random_no_4 = random_no[new_variable]
print('切割第1246行:{}'.format(random_no_4))
random_no[random_no < 0] = 0
print('random_no < 0:{}'.format(random_no))
random_no[personals != 'Manu'] = 9
print("personals != 'Manu':{}".format(random_no))



algebra = random.randn(7, 4)
print('algebra:{}'.format(algebra))
for j in range(7):
    algebra[j] = j

print(algebra)
print('选取5 6 2行:{}'.format(algebra[[4, 5, 1]]))
fancy = np.arange(36).reshape(9, 4)
print(fancy)
fancy_1=fancy[[4, 3, 2, 1],[3, 2, 2, 2]]
print("列表截取指定行列:{}".format(fancy_1))
fancy_3=fancy[[1, 4, 8, 2]]
fancy_2=fancy[[1, 4, 8, 2]][:, [0, 3, 1, 2]]
print("列表截取指定行:{}".format(fancy_3))
print("列表截取指定行，重新安排列的位置:{}".format(fancy_2))
fancy_4=fancy[np.ix_([1,4,8,2],[0,3,1,2])]
print("用np.ix function截取指定行，重新安排列的位置:{}".format(fancy_4))


#Transposing Arrays
transpose = np.arange(12).reshape(3, 4)
print("Original's arrays:{}".format(transpose))
print("transpose.T:{}".format(transpose.T))



#universal functions
funky = np.arange(8)
print(funky)
print(np.sqrt(funky)) #平方根
print(np.exp(funky)) #返回以e为底

x = random.randn(10)
y = random.randn(10)
print(x)
print(y)
print(np.maximum(x, y))
print(np.modf(x))
print(np.abs(x))


#Data processing using Arrays
mtrices = np.arange(-5, 5, 1)
x, y = np.meshgrid(mtrices, mtrices)
print("Matrix values of y:{}".format(y))
print("Matrix values of x:{}".format(x))

x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([6, 7, 8, 9, 10])
cond = [True, False, True, True, False]
z1 = [(x, y, z) for x, y, z in zip(x1, y1, cond)]
print(z1)
print(np.where(cond, x1, y1)) #where进行条件判断

ra = np.random.randn(5, 5)
print(ra)
print(np.where(ra>0, 1, -1))
print(np.where(ra>0, 1, ra))



#Statistical methods
thie = np.random.randn(5, 5)
print(thie.mean())
print(np.mean(thie))
print(thie.sum())
jp=np.arange(12).reshape(4, 3)
print("The arrays are:{}".format(jp))
print("The sum of columns are:{}".format(np.sum(jp, axis=0)))
print("The sum of rows are:{}".format(np.sum(jp, axis=1)))
print("The sum of rows are:{}".format(jp.sum(0)))
print("cumulative sum of columns:{}".format(jp.cumsum(0)))
print("cumulative sum of rows:{}".format(jp.cumsum(1)))
xp = np.random.randn(100)
print((xp > 0).sum())
print((xp < 0).sum())
tandf = np.array([True, False, True, False, True, False])
print(tandf.any())
print(tandf.all()) #判断是否全为True


#Sorting
lp = np.random.randn(8)
print("lp:{}".format(lp))
lp.sort()
print("对lp进行排序:{}".format(lp))
tp = np.random.randn(4, 4)
print("tp:{}".format(tp))
tp.sort(1)
print("对tp按行进行排序:{}".format(tp))
personals = np.array(['Manu', 'Jeevan', 'Prakash', 'Manu', 'Prakash', 'Jeevan', 'Prakash'])
print(np.unique(personals))
print(set(personals))
# print(type(np.unique(personals)))
# print(type(set(personals)))

personals_Manu=np.in1d(personals, ['Manu'])
print(personals_Manu)


#Linear Algebra
cp = np.array([[1, 2, 3], [4, 5, 6]])
dp = np.array([[7, 8], [9, 10], [11,12]])
print("CP array:{}".format(cp))
print("DP array:{}".format(dp))
print("两矩阵相乘:{}".format(cp.dot(dp)))
print("两矩阵相乘:{}".format(np.dot(cp, dp))) #另一种个写法
print(np.ones(3))
print(np.dot(cp, np.ones(3)))

from numpy.linalg import inv, qr
cp = np.array([[1,2,3], [4,5,6]])
new_mat = cp.T.dot(cp) #乘自己的转置矩阵
print(new_mat)
sp = np.random.randn(5, 5)
print("sp:{}".format(sp))
print(inv(sp))
print(sp.dot(inv(sp)))
q, r = qr(sp)
print(q)
print(r)


score = np.ones(10, dtype=np.int) #dtype规定字符类型
print(score)