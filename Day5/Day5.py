'''
                            DATA HANDLING
Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
A Pandas Series is like a column in a table.It is a one-dimensional array holding data of any type.
A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
Series is like a column, a DataFrame is the whole table.
Pandas use the loc attribute to return one or more specified row(s)
'''
import pandas as pd

x=(1,2,3,4)
myval=pd.Series(x)
print(myval)

x=[(1,2),('a','b')]
myval=pd.Series(x)
print(myval)  #print values in pair
print(myval[1])

x=[(1,2),('a','b')]
myval=pd.Series(x, index=('numbers','alphabets'))  #giving our own labels
print(myval)
print(myval[1])   
print(myval['numbers'])

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)    #keys becomes indexes
print(myvar)

calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories, index = ["day1", "day2"])  #Creat a Series using only data from "day1" and "day2"
print(myvar)

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data)
print(df) 
print(df.loc[1])  #returns a pandas Series
print(df.loc[[1,2]])  #When using [], the result is a Pandas DataFrame.


data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index=("day1", "day2", "day3"))  #giving our own labels
print(df) 
print(df.loc['day1'])  
print(df.loc[['day1','day2']]) 

'''
                            FILE HANDLING
The key function for working with files in Python is the open() function.
The open() function takes two parameters; filename, and mode.
There are four different methods (modes) for opening a file:
"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists
In addition you can specify if the file should be handled as binary or text mode
"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
The open() function returns a file object, which has a read() method for reading the content of the file.
You can return one line by using the readline() method.
close() - to close the file.
write() - to write to a file.
To delete a file, you must import the OS module, and run its os.remove() function
To delete an empty directory, you must import the OS module, and run its os.rmdir() function
'''
#1) Count the number of lines in a file

def count():
    f=open('file.txt')
    c=0
    for i in f:
        c+=1
    print("The number of lines in the file are:",c)
    f.close()

#2) Count the number of characters in a file

def count():
    f=open('file.txt')
    c=0
    for i in f:
        for x in i:
            c+=1
    print("The number of characters in the file are:",c)
    f.close()
#3) Replace the content of one file with the other

def copy():
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file before update:",data)
    f1=open('file.txt','w')
    f2=open('file2.txt')
    data=f2.read()
    f1.write(data)
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file after update:",data)
    f1.close()
    f2.close()

#4) Find the sum of the space separated numbers entered in a file
def findsum():
    f1=open('file3.txt')
    data = f1.read()
    x=data.split()
    i = list(map(int, x))
    print('Sum of values is:',sum(i))
    f1.close()

#5) Append the content of one file in another
def copy():
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file before update:",data)
    f1=open('file.txt','a')
    f2=open('file2.txt')
    data=f2.read()
    f1.write(data)
    f1=open('file.txt')
    data=f1.read()
    print("Contents of file after update:",data)
    f1.close()
    f2.close()
    

'''
                            Database Connectivity
Python needs a MySQL driver to access the MySQL database:- we will use the driver "MySQL Connector".
pip install mysql-connector-python

The MySQLCursor of mysql-connector-python (and similar libraries) is used to execute statements to communicate with the MySQL database.
Using the methods of it you can execute SQL statements, fetch data from the result sets, call procedures.
You can create Cursor object using the cursor() method of the Connection object/class.

Note the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
T
o insert multiple rows into a table, use the executemany() method.
The second parameter of the executemany() method is a list of tuples, containing the data you want to insert

fetchall() method, which fetches all rows from the last executed statement.
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result

mycursor.lastrowid, mycursor.rowcount
You can also select the records that starts, includes, or ends with a given letter or phrase.

Use the %  to represent wildcard characters

It is considered a good practice to escape the values of any query
This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
The mysql.connector module uses the placeholder %s to escape values
'''
import mysql.connector

mydb=mysql.connector.connect(       #connecting to server
    host="localhost",
    user="root",
    password="nancy@123"
)
mycursor=mydb.cursor()
mycursor.execute("CREATE database students")

#connecting to db
mydb=mysql.connector.connect( 
    host="localhost",
    user="root",
    password="nancy@123",
    database="students"
)
mycursor=mydb.cursor()
mycursor.execute('SHOW DATABASES')
for x in mycursor:
    print(x)

#creating table
mycursor.execute('SHOW Tables')
for x in mycursor:
    print(x)

mycursor.execute("CREATE TABLE stud (id Int, name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("ALTER TABLE stud MODIFY id INT AUTO_INCREMENT PRIMARY KEY")   #field modified
#adding one record
sql = "INSERT INTO stud (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print('Number of rows added:',mycursor.rowcount)
print('Last added row id:',mycursor.lastrowid)

#adding multiple records
sql = "INSERT INTO stud (name, address) VALUES (%s,%s)"
val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]
mycursor.executemany(sql,val)
mydb.commit()
print('Number of rows added:',mycursor.rowcount)
print('Last added row id:',mycursor.lastrowid)

#retrieving all the records from db
mycursor.execute("SELECT * FROM stud")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#retrieving selected columns from db
mycursor.execute("SELECT id,name FROM stud")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#retrieving only one record from db
mycursor.execute("SELECT * FROM stud")
myresult = mycursor.fetchone()
print(myresult)

#retrieving only one record from db
mycursor.execute("SELECT id, name FROM stud")
myresult = mycursor.fetchone()
print(myresult)

#using WHERE
mycursor.execute("SELECT * FROM stud WHERE address ='Park Lane 38'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
#using placeholder to prevent injection
sql="SELECT * FROM stud WHERE address =%s"
val=('Park Lane 38',)
mycursor.execute(sql,val)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#using WHERE
mycursor.execute("SELECT * FROM stud WHERE name LIKE '%na%'")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#using ORDER BY and DESC
mycursor.execute("SELECT * FROM stud ORDER BY name DESC")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#Using DELETE
sql = "DELETE FROM stud WHERE name = %s"
val=("Michael" ,)
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted!")

#UPDATE table
sql = "UPDATE stud SET address = %s WHERE address = %s"
val = ("Valley 345", "Park Lane 38")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#LIMIT AND OFFSET
mycursor.execute("SELECT * FROM stud LIMIT 5 OFFSET 5")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

#DROP TABLE
sql = "DROP TABLE IF EXISTS stud"
mycursor.execute(sql)

