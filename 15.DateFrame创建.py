import pandas as pd

data1={
    'Name':['小明','小红','杰瑞','汤姆'],
    'Age':[18,19,30,29],
}

rank=['student1','student2','student3','student4']
#创建方法1
df1=pd.DataFrame(data1,index=rank)#字典作为传入的数据
print(df1)

#创建方法2
data2=[['小明',18],['小红',19],['杰瑞',30],['汤姆',29]]
df2=pd.DataFrame(data2,index=rank,columns=['Name','Age'])#列表作为传入的数据，需要单独加上行索引
print(df2)

#创建方法3
s1=pd.Series(['小明','小红','杰瑞','汤姆'])
s2=pd.Series([18,19,30,29])
df3=pd.DataFrame({'Name':s1,'Age':s2},index=rank)
print(df3)

#新增一列
df1['性别']=['男','女','男','男']
print(df1)

#新增一行
new_row=pd.DataFrame([{'性别':'男','Age':'20','Name':'花花'}],
                     index=['student5'])
df=pd.concat([df1,new_row])
print(df)

