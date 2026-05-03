import pandas as pd
data={
    'Name':['小明','小红','杰瑞','汤姆'],
    'Age':[18,19,30,29],
}

rank=['student1','student2','student3','student4']

df=pd.DataFrame(data,index=rank)
print(df)

print(df.index)
print(df.values)
print(df.dtypes)
print(df.shape)
print(df.ndim)
print(df.size)
print(df.columns)
print(df.T)
#获取某行或某列数据
#某行
print(df.loc['student1'])
print(df.iloc[0])
#某列
print(df.loc[:,'Name'])
print(df.iloc[:,0])
#获取单个数据
print(df.at['student2','Age'])
print(df.iat[1,1])
print(df.loc['student2','Age'])
print(df.iloc[1,1])