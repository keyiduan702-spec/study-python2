import pandas as pd
data={
    'Name':['小明','小红','杰瑞','汤姆'],
    'Age':[18,19,30,29],
}

rank=['student1','student2','student3','student4']

df=pd.DataFrame(data,index=rank)
print(df)
#获取单列数据
print(df['Name'])
print(type(df['Name']))
print(df.Name)
print(type(df.Name))
#获取多列数据
print(df[['Name','Age']])
#查看部分数据
print(df.head(2))
print(df.tail(2))
#布尔索引筛选数据
print(df[df.Age>18])
print(df[(df.Age>18)&(df.Age<30)])
#随机取样
print(df.sample())
print(df.sample(2))