import numpy as np
arr=np.random.randint(1,100,6)
print(arr)
#排序函数
print(np.sort(arr))#升序排列
print(np.argsort(arr))#数对应的索引值升序排列

#去重函数
print(np.unique(arr))

#数组的拼接
arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
print(arr1+arr2)
print(np.concatenate((arr1,arr2)))

#数组的分割
print(np.split(arr,3))#分割成3份
print(np.split(arr,[2]))#在下标 2 的位置切开
print(np.split(arr,[2,3]))#在下标2和3处切开


