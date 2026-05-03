import pandas as pd
arr1=['小明','小红','汤姆','李贝','杰瑞','熊大','熊二']
arr2=[12,34,78,None,100,100,100]

s=pd.Series(arr2,index=(arr1))
print(s)

print(s.head(1))
print(s.tail(1))
print(s.isin([12]))#判断元素是否在参数集合里面，
#isin() 方法的参数必须是可迭代对象（列表、元组、集合等）
print(s.isna())#判断是否为缺失值
print(s.sum())
print(s.mean())#平均数
print(s.min())
print(s.max())
print(s.var())#方差
print(s.std())#标准差
print(s.median())#中位数
print(s.mode())#众数
print(s.quantile(0.2))#百分之20分位数
print(s.describe())#显示常见的统计信息