import numpy as np
arr = np.array([1,2,3,4,5])

#方式1：布尔索引筛选
mask = arr>3
print(mask)
filtered = arr[mask]
print(filtered)
#即print(arr[arr>3])

#方式2:用np.where替换/筛选

#筛选
indices = np.where(arr>3)
print(indices)
print(arr[indices])
#即print(arr[np.where(arr>3)])

#筛选+替换
result = np.where(arr>3,10,0)#大于3的替换为10，否则为0
print(result)

#实例
ages=np.array([[21,17,19,20,53],
               [23,53,82,10,19]])
teenagers=np.where(ages>=18,ages,0)
print(teenagers)