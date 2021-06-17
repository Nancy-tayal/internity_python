'''
Pandas is an open-source Python Library providing high-performance data manipulation and analysis tool using its powerful data 
structures. The name Pandas is derived from the word Panel Data – an Econometrics from Multidimensional data.
Using Pandas, we can accomplish five typical steps in the processing and analysis of data, regardless of the origin of data — load, 
prepare, manipulate, model, and analyze.

'''

#Series

import pandas as pd

s=pd.Series()
print(s) #Series([], dtype: float64)

s=pd.Series([1,2,3,4,5])
print(s)

s=pd.Series([1,'a',3,'4',5])
print(s)
'''
0    1
1    a
2    3
3    4
4    5
dtype: object
'''
s=pd.Series([1,'a',3,'4',5], index=[8,9,5,3,2])
print(s)
print(s[0])
print(s[8])
print(s[0:3])
'''
8    1
9    a
5    3
3    4
2    5
dtype: object
KeyError: 0
1
8    1
9    a
5    3
print(s[0:3])

'''

s=pd.Series([1,'a',3,'4',5], index=['a','b','c','d','e'])
print(s)
print(s[0])
print(s['a'])
print(s[0:3])
print(s['f'])
print(s[[0,2,4]])
'''
a    1
b    a
c    3
d    4
e    5
dtype: object
1
1
a    1
b    a
c    3
dtype: object
KeyError: 'f'
a    1
c    3
e    5
dtype: object
'''
s=pd.Series(4)
print(s) #0  4
s=pd.Series(4,index=[1,2,3,4])
print(s)
'''
1    4
2    4
3    4
4    4
dtype: object
'''
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
print(s)
print(s['a'])
print(s[0])

'''
a    0.0
b    1.0
c    2.0
dtype: float64
0.0
0.0
'''

data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
print(s)
print(s[2])
'''
b    1.0
c    2.0
d    NaN
a    0.0
dtype: float64
nan
'''

#DataFrames
df = pd.DataFrame()
print(df)
'''
Empty DataFrame
Columns: []
Index: []
'''
#creating dataframe from python lists
data = [1,2,3,4,5]
df = pd.DataFrame(data)
print(df)
'''
   0
0  1
1  2
2  3
3  4
4  5
'''
#using list of lists
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
print (df)
'''
     Name  Age
0    Alex   10
1     Bob   12
2  Clarke   13
'''

#using Dictionary
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
print(df)
'''
    Name  Age
0    Tom   28
1   Jack   34
2  Steve   29
3  Ricky   42
'''
#using list of dictonaries
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])
print(df1)
print(df2)
'''
        a   b
first   1   2
second  5  10
        a  b1
first   1 NaN
second  5 NaN
'''
#using a dictionary of series
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df)
'''
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
'''

#using a csv  file
df = pd.read_csv('data.csv')
print(df.to_string()) 
'''
   Total Grade
0      0  Fail
1     36     E
2     54     D
3     72     C
4     80     B
5     92     A
'''

#using a json file
df = pd.read_json('data.json')
print(df.to_string())
'''
   Duration  Pulse  Maxpulse  Calories
0        60    110       130       409
1        60    117       145       479
2        60    103       135       340
3        45    109       175       282
4        45    117       148       406
5        60    102       127       300
'''

#using a database
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="nancy@123",
    database='emp')

df=pd.read_sql("select * from Employee", mydb)
print(df)

'''
    PName         Street      City Email
0    Hope    Alma street    London  None
1    Jack  Bakers street     Paris  None
2     Kim    Adam street     Paris  None
3  Landon    Adam street     Paris  None
4     Liz  Bakers street  New York  None
5     Tim    Alma street    London  None
'''
#using a dataframe
df2=pd.DataFrame(df)
df3=pd.DataFrame({'PName':['Lean'],'Street':['Bakers street'],'City':['Japan'],'Email':['None']})
df2=df2.append(df3)
print(df2)
'''
    PName         Street      City Email
0    Hope    Alma street    London  None
1    Jack  Bakers street     Paris  None
2     Kim    Adam street     Paris  None
3  Landon    Adam street     Paris  None
4     Liz  Bakers street  New York  None
5     Tim    Alma street    London  None
0    Lean  Bakers street     Japan  None
'''
#summarizing data
print(df2.info())
print(df2.describe())
'''
<class 'pandas.core.frame.DataFrame'>
Int64Index: 7 entries, 0 to 0
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   PName   7 non-null      object
 1   Street  7 non-null      object
 2   City    7 non-null      object
 3   Email   1 non-null      object
dtypes: object(4)
memory usage: 280.0+ bytes
None

         PName         Street   City Email
count        7              7      7     1
unique       7              3      4     1
top     Landon  Bakers street  Paris  None
freq         1              3      3     1
'''

#using an API
df=pd.read_json("http://ccdb.hemiola.com/")
print(df)



'''
PANEL
A panel is a 3D container of data. The term Panel data is derived from econometrics and is partially responsible 
for the name pandas − pan(el)-da(ta)-s.
The names for the 3 axes are intended to give some semantic meaning to describing operations involving panel data. They are −
items − axis 0, each item corresponds to a DataFrame contained inside.
major_axis − axis 1, it is the index (rows) of each of the DataFrames.
minor_axis − axis 2, it is the columns of each of the DataFrames.
'''
import numpy as np
p=pd.Panel()
print(p)
'''
<class 'pandas.core.panel.Panel'>
Dimensions: 0 (items) x 0 (major_axis) x 0 (minor_axis)
Items axis: None
Major_axis axis: None
Minor_axis axis: None
'''
data = np.random.rand(2,4,5)
p = pd.Panel(data)
print(p)
'''
<class 'pandas.core.panel.Panel'>
Dimensions: 2 (items) x 4 (major_axis) x 5 (minor_axis)
Items axis: 0 to 1
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 4
'''
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p)
'''
Dimensions: 2 (items) x 4 (major_axis) x 3 (minor_axis)
Items axis: Item1 to Item2
Major_axis axis: 0 to 3
Minor_axis axis: 0 to 2
'''