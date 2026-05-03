import pandas as pd
s=pd.Series([1,2,3,4,5,6,7],index=['a','b','c','d','e','f','g'])
print(s)

print(s['a'])#通过标签索引
print(s.loc['a'])#显示索引
print(s.iloc[0])#隐式索引
print(s.head(1))#查看前1行
print(s.tail(2))#查看后2行
print(s[s>5])#布尔索引