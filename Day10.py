#Accessing, reading a nd writing data in Series
import pandas as pd

s=pd.Series([1,'a',3,'4',5], index=[8,9,5,3,2])
print(s)
print(s[0])
print(s[8])
print(s[0:3])
s[0]=7
print(s)
s[1:4]=[1,2,3]
print(s)
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
dtype: object
8    1
9    a
5    3
3    4
2    5
0    7
dtype: object
8    1
9    1
5    2
3    3
2    5
0    7
dtype: object
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

#Accessing, reading and writing data in Panels

import numpy as np
data = {'Item1' : pd.DataFrame(np.random.randn(4, 3)), 
   'Item2' : pd.DataFrame(np.random.randn(4, 2))}
p = pd.Panel(data)
print(p['Item1'])
print(p.major_xs(1))
print(p.minor_xs(1))

'''
          0         1         2
0 -0.983897 -0.538192  0.869140
1  1.057142  0.183670 -1.071166
2  1.271447  0.919718  2.238118
3  0.586175  0.541718 -1.482218 

      Item1     Item2
0  1.057142 -0.852167
1  0.183670 -0.049891
2 -1.071166       NaN 

      Item1     Item2
0 -0.538192  0.500083
1  0.183670 -0.049891
2  0.919718 -1.543254
3  0.541718 -0.950062
'''

#Acessing, reading, writing, indexing and slicing data in DataFrames
d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
   'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(d)
print(df['one']) 
print(df[['one','two']])
'''
   one 
a  1.0    
b  2.0    
c  3.0    
d  NaN    
Name: one, dtype: float64
   one  two
a  1.0    1
b  2.0    2
c  3.0    3
d  NaN    4
'''
#adding a new column
df['three']=pd.Series([3,6,9,12], index=['a','b','c','d'])
print(df)
'''
   one  two  three
a  1.0    1      3
b  2.0    2      6
c  3.0    3      9
d  NaN    4     12
'''
df['four']=df['two']+df['three']
print(df)
'''
   one  two  three  four
a  1.0    1      3     4
b  2.0    2      6     8
c  3.0    3      9    12
d  NaN    4     12    16
'''
#Deleting columns
del df['one']
df.pop('two')
print(df)
'''
   three  four
a      3     4
b      6     8
c      9    12
d     12    16
'''

#accessing and slicing rows
print(df.loc['b'])
print(df.iloc[1])
print(df.loc['a','three'])
'''
three    6
four     8
Name: b, dtype: int64
three    6
four     8
Name: b, dtype: int64
3
'''
print(df[1:3])
'''
   three  four
b      6     8
c      9    12
'''

#adding and deleting rows
df=df.append(pd.DataFrame([[7,8]], index=['e'], columns=['three', 'four']))
print(df)
'''
   three  four
a      3     4
b      6     8
c      9    12
d     12    16
e      7     8
'''
df=df.append(pd.DataFrame([[7,8]], index=['e'], columns=['three', 'four']))
print(df)
df=df.drop('e')
print(df)
'''
   three  four
a      3     4
b      6     8
c      9    12
d     12    16
e      7     8
e      7     8
   three  four
a      3     4
b      6     8
c      9    12
d     12    16
'''

#cleaning data
'''
Bad data could be:

Empty cells
Data in wrong format
Wrong data
Duplicates
'''

df = pd.read_csv('data.csv')
df.dropna(inplace = True)   #removing rows with NaN or None values i.e. empty values in the entire dataframe
print(df.to_string())
df['Date']=pd.to_datetime(df['Date'])
df.dropna(subset=['Date'], inplace = True) #removing rows with NaN or None values i.e. empty values on the basis of values in the Date column


df = pd.read_csv('data.csv')
df.fillna(0,inplace = True)   #replacing empty cell with the data passed
print(df.to_string())
df['Duration'].fillna(0,inplace=True)   #replacing null values in the specified columns
print(df.to_string())

#we can replace the empty cells of a column with the mean(), median() or mode of that column
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True)
x = df["Calories"].mode()[0]    #mode may contain multiple values 
df["Calories"].fillna(x, inplace = True)

df=df[~df['Duration'].isna()] #Removes all the rows in which the duration is NaN or None
df=df[~df['Duration'].isnull()] #Removes all the rows in which the duration is NaN or None
df=df[~df.isna().any(axis=1)] #Removes all the rows rows with NaN under an entire DataFrame
df=df[~df.isnull().any(axis=1)] #Removes all the rows rows with NaN under an entire DataFrame
for x in df.index: 
  if df.loc[x, "Duration"] > 120:
    df.drop(x, inplace = True)  #deleting rows with wrong values in the duration col
for x in df.index: 
  if df.loc[x, "Duration"] > 120:
    df.loc(x, "Duration") = df["Duration"].mode()[0]  #replacing the wrong values
df.drop_duplicates(inplace = True) #Removing all the rows containing duplicate data

#aggregate
df=pd.read_json('data.json')
print(df.to_string())
df.aggregate(['sum','min'])
'''
   Duration  Pulse  Maxpulse  Calories
0        60    110       130       409
1        60    117       145       479
2        60    103       135       340
3        45    109       175       282
4        45    117       148       406
5        60    102       127       300
     Duration  Pulse  Maxpulse  Calories
sum       330    658       860      2216
min        45    102       127       282
'''
df.aggregate({"Duration":['sum', 'min','mean'],
              "Pulse":['max', 'min'],
              "Maxpulse":['min', 'sum'], 
              "Calories":['sum','mean']})
'''
      Duration  Pulse  Maxpulse     Calories
sum      330.0    NaN     860.0  2216.000000
min       45.0  102.0     127.0          NaN
max       55.0  117.0       NaN          NaN
mean       NaN    NaN       NaN   369.333333
'''

#Pandas provides a single function, merge, as the entry point for all standard database join operations between DataFrame objects.
df1 = pd.DataFrame({
   'id':[1,2,3,4,5],
   'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
   'subject_id':['sub1','sub2','sub4','sub6','sub5']})
df2 = pd.DataFrame({
	'id':[1,2,3,4,5],
   'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
   'subject_id':['sub2','sub4','sub3','sub6','sub5']})

df3=pd.merge(df1,df2,on='id')   #joining on single column
print(df3)
'''
   id  Name_x subject_id_x Name_y subject_id_y
0   1    Alex         sub1  Billy         sub2
1   2     Amy         sub2  Brian         sub4
2   3   Allen         sub4   Bran         sub3
3   4   Alice         sub6  Bryce         sub6
4   5  Ayoung         sub5  Betty         sub5
'''
df3=pd.merge(df1,df2,on=['id','subject_id'])    #joining on multiple columns (default inner join)
print(df3)
'''
   id  Name_x subject_id Name_y
0   4   Alice       sub6  Bryce
1   5  Ayoung       sub5  Betty
'''
df3=pd.merge(df1,df2,on=['id','subject_id'], how='left')    #Left Outer join
print(df3)
'''
   id  Name_x subject_id Name_y
0   1    Alex       sub1    NaN
1   2     Amy       sub2    NaN
2   3   Allen       sub4    NaN
3   4   Alice       sub6  Bryce
4   5  Ayoung       sub5  Betty
'''

df3=pd.merge(df1,df2,on=['id','subject_id'], how='right')    #Right Outer join
print(df3)
'''
   id  Name_x subject_id Name_y
0   1     NaN       sub2  Billy
1   2     NaN       sub4  Brian
2   3     NaN       sub3   Bran
3   4   Alice       sub6  Bryce
4   5  Ayoung       sub5  Betty
'''
df3=pd.merge(df1,df2,on=['id','subject_id'], how='outer')    #Outer join
print(df3)
'''
   id  Name_x subject_id Name_y
1   2     Amy       sub2    NaN
2   3   Allen       sub4    NaN
3   4   Alice       sub6  Bryce
4   5  Ayoung       sub5  Betty
5   1     NaN       sub2  Billy
6   2     NaN       sub4  Brian
7   3     NaN       sub3   Bran
'''


