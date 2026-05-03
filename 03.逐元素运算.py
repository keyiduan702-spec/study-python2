import numpy as np
a1 = np.array([[1,2,3],
              [5,6,7]])
a2 = np.array([4,5,6])

#一维数组运算
#数组 + 数字 （标量运算）
#所有元素一起算，不用写循环
print(a2+4)
print(a2-4)
print(a2*2)
print(a2/4)
#数组 + 数组（同形状）
#对应位置运算
a3 = np.array([1,2,3])
print(a2+a3)
print(a2-a3)
print(a2*a3)
print(a2/a3)

#二维数组运算
#二维+数字
print(a1+2)
#二维+二维
a4 = np.array([[2,4,6],
               [1,3,5]])
print(a1+a4)
print(a1*a4)




