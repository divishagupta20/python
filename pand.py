import pandas as pd

data = [1,2,3.5,"hellooooo"]

arr = pd.Series(data)

dic = {'a':1,'b':5,'c':3}
series_dict = pd.Series(dic)
print(series_dict)

dic = {
    'name': ['krish','john','jack'],
    'age' :  [34,6,78],
    'city' : ["delhi","bombay","new york"]
    }
df = pd.DataFrame(dic)
print(df)

dic = [
    {'name' : 'divisha','age':56,'city':'delhi'},
    {'name' : 'divisha','helooo':56,'city':'delhi'},
    {'name' : 'divisha','age':56,'city':'delhi'}
]

print(dic[0]['name'])

df = pd.DataFrame(dic)
print(df)

df = pd.read_csv('example.csv')
print(df.head(1))
print(df)

print(df.loc[0])
print(df.iloc[0])

import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'C'],
    'Marks': [80, 90, 100]
}, index=['x', 'y', 'z'])

print(df)
print(df.loc['x'])
print(df.iloc[0])
print(df.at['y','Marks'])

print(df.iat[2,1]) 

df['salary'] = [567,352,325]
print(df)

df.drop('salary',axis=1,inplace=True)
print(df)

df['Marks'] = df['Marks']+1
print(df)
df.drop('x',inplace=True)
print(df)