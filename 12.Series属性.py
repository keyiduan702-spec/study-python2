import pandas as pd

i = [1,2,3,4,5]
num = [71,85,92,85,84]

grade=pd.Series(num,index=(i))
print(grade)

print(grade.index)
print(grade.values)
print(grade.dtype)
print(grade.shape)
print(grade.ndim)
print(grade.size)
grade.name='test'
print(grade.name)
print(grade.loc[1])#显示索引
print(grade.loc[1:2])
print(grade.iloc[0])#隐式索引
print(grade.iloc[0:2])
print(grade.at[1])#使用标签访问单个元素，不支持切片
print(grade.iat[0])#使用位置访问单个元素，不支持切片


