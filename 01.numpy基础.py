import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([[1,2,3,4,5],
            [6,7,8,9,10]])

#numpy属性
print('a的形状是',a.shape)
print('b的形状是',b.shape)

print('a的维度是',a.ndim)
print('b的维度是',b.ndim)

print('a的总元素个数是',a.size)
print('b的总元素个数是',b.size)

print('a的元素类型是',a.dtype) 
print('b的元素类型是',b.dtype)

print('a的转置是',a.T)
print('b的转置是',b.T)

#numpy的创建
#1.基础构造
print(np.array([[1,2,3],[4,5,6]]))
print(np.copy(a))
#2.预定义形状填充
print(np.zeros((2,3)))
print(np.zeros((2,3),dtype=np.int64))

print(np.ones((2,3)))
print(np.ones((2,3),dtype=np.int64))

print(np.empty((2,3)))

print(np.full((2,3),5))
#3.模仿b的形状填充
print(np.zeros_like(b))
print(np.ones_like(b))
print(np.empty_like(b))
print(np.full_like(b,5))

#4.等差数列
print(np.arange(2,11,2))
#5.等间隔数列
print(np.linspace(1,10,3))#在1到10之间取3份

#数组重塑
#1.reshape()重塑形状
arr1=np.array([1,2,3,4,5,6,7,8,9,10])
print(arr1)
arr2=arr1.reshape(2,5)#重塑成2行5列
print(arr2)

arr3=arr1.reshape(5,-1)#固定为5行，列自动算
print(arr3)
arr4=arr1.reshape(-1,5)#固定为5列，行自动算
print(arr4)

#2.flatten()扁平化：把任意数组压缩为一维数组
b1=np.array([[1,2,3],
             [4,5,6]])
print(b1)
b2=b1.flatten()
print(b2)

