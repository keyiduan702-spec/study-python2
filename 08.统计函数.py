import numpy as np
arr = np.random.randint(1,20,8)
print(arr)

#求和
print(np.sum(arr))

#计算平均值
print(np.mean(arr))

#计算中位数
print(np.median(arr))

#计算标准差、方差
print(np.var(arr))
print(np.std(arr))

#计算最大值、最小值
print(np.max(arr))
print(np.argmax(arr))#最大值的数的索引
print(np.min(arr))
print(np.argmin(arr))#最小值的数的索引

#计算分位数
print(np.percentile(arr,20))#20% 分位数

#计算累计和、累积积
b=np.array([1,2,3,4])
print(np.cumsum(b))
print(np.cumprod(b))