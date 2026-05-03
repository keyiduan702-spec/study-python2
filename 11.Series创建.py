import pandas as pd

GDP=[80855,77388,68024,47251,40471]
city=['GD','JS','SD','ZJ','HN']

#创建一个Series
#pd.Series(数据，索引)
print(pd.Series(GDP))
info=pd.Series(GDP,index=city)
print(info)

#通过字典创建
aclories = {'Day1':170,'Day2':20,'Day3':300}
series=pd.Series(aclories)
print(series)
