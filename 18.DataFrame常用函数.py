import pandas as pd
data={
    'Name':['小明','小红','杰瑞','汤姆'],
    'Age':[18,19,30,29],
}

rank=['student1','student2','student3','student4']

df=pd.DataFrame(data,index=rank)
print(df)

print(df.head(2))
print(df.tail(2))
print(df['Age'].sum())
print(df['Age'].mean())
print(df['Age'].min())
print(df['Age'].max())
print(df['Age'].var())
print(df['Age'].std())
print(df['Age'].median())
print(df['Age'].mode())
print(df['Age'].quantile(0.1))
print(df['Age'].describe())
print(df.isin(['小红']))
print(df.isna())