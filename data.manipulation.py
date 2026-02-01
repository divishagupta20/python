import pandas as pd

df = pd.read_csv('example.csv')

print(df.describe())
print(df.isnull())
print(df.isnull().any(axis=1)) #every record
print(df.isnull().sum())
df.fillna(0,inplace=True)
print(df)
df['sales'] = df['Gender'].fillna(df['Year'].mean())
print(df)
print(df.dtypes)
df.rename(columns={'Year':'holidays'},inplace=True)
print(df)
df['holidays']=df['holidays'].astype(float)
print(df.dtypes)

df['year'] = df['holidays'].apply(lambda x:x*2);
print(df.head(4))
print(df.groupby(['Gender','City'])['year'].mean())
print(df.groupby(['Gender'])['year'].mean())
print(df.groupby(['Gender'])['year'].agg(['mean','sum','count']))

df1 = pd.DataFrame({'key' : ['a','b','c'],'value1' : [1,3,4]})
df2 = pd.DataFrame({'key' : ['a','b','D'],'value2' : [5,2,6]})
df3 = pd.merge(df1,df2,on='key',how='inner')
print(df3)
df3 = pd.merge(df1,df2,on='key',how='outer')
print(df3)
df3 = pd.merge(df1,df2,on='key',how='left')
print(df3)
df3 = pd.merge(df1,df2,on='key',how='right')
print(df3)
print(df['year'].agg(['mean','sum']))

df.to_csv('user.csv')
