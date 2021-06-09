#Functions and Modules

#1) Write a Python program to reverse a string.
def revstr():
    str=input("Enter a string to be reversed: ")
    st=""
    for i in range(len(str)-1,-1,-1):
        st=st + str[i]
    print("Reverse of input string is:",st)

#2)Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
def count():
    str=input("Enter a string: ")
    lower=upper=0
    for i in str:
        if i.isupper():
            upper+=1
        elif i.islower():
            lower+=1
    print('UpperCase Character Count:',upper)
    print('LowerCase Character Count:',lower)

#3)Write a Python function that takes a list and returns a new list with unique elements of the first list.
def remove_duplicates():
    length=int(input("Enter the length of the list: "))
    l=[]
    for i in range(length):
        print("enter item number",i+1)
        inp=int(input())
        l.append(inp)
    for i in l:
        x=l.count(i)
        if x>1:
            while x!=1:
                l.remove(i)
                x-=1
    print(l)

#4)Calculate addition, subtraction, multiplication, division of two numbers using modules


 #naming it as arithmetic.py

import arithmetic as ar

print(ar.add(2,4)) # 6
print(ar.sub(2,4)) # -2

from arithmetic import mul,div
print(ar.mul(2,4)) # 8
print(ar.div(2,4)) # 0.5

#5) Write a Python function that checks whether a passed string is palindrome or not.
def pallindrome():
    str=input("Enter a string to be reversed: ")
    st=""
    for i in range(len(str)-1,-1,-1):
        st=st + str[i]
    if(str==st):
        print("Reverse of input string is:",st,'and Hence a Pallindrome')
    else:
        print('Not a pallindrome')

#List Comprehensions

#1) Print all the list elements using list comprehensions
l=[1,3,5,7,9]
y=[print(x) for x in l]
print(y)#[None, None, None, None, None] print returns None

#2)calculate the squares of list numbers using list comprehensions
l=[1,3,5,7,9]
y=[x*x for x in l]
print(y)


#3)calculate the product of list1 items wth the all the items of list2 using list comprehensions
l1=[1,3,5,7,9]
l2=[0,2,4,6,8]
y=[x*w for x in l1 for w in l2]
print(y)

#4)create a list consisting of a postive subset of a given list using list comprehensions
l=[1,3,-5,7,-9, 8,-3]
y=[x for x in l if x>0]
print(y)

#5)convert the string to uppercase using list comprehensions
str="Nancy Tayal"
y=[x.upper() for x in str]
st="".join(y)
print(st) # Nancy Tayal

#iterators

#1) Use a infinite stream custom iterator to first 10 generate odd numbers
class Odd:
    
    def __init__(self):
        self.odd=0
    
    def __iter__(self):
        self.odd=1
        return self
    
    def __next__(self):
        result=self.odd
        self.odd+=2
        return result
    
odd=Odd()
y=iter(odd)
for i in range(10):
    print(next(y))

#1) Re-write the above code while raising an StopIteration error if the limit exceedes
class Odd:
    
    def __init__(self,max):
        self.max=max
    
    def __iter__(self):
        self.odd=1
        return self
    
    def __next__(self):
        if self.odd<self.max*2:
            result=self.odd
            self.odd+=2
            return result
        else:
            raise StopIteration

odd=Odd(10)
y=iter(odd)
for i in range(11):
    print(next(y)) #an error is raised at the 11th iteration

#3)print all the elements of list using iterator
l=[1,2,3,4,5]
itr=iter(l)
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

#4)print all the characters in uppercase of a string using iterator
str=input("Enter a string: ")
itr=iter(str)
while True:
    try:
        print(next(itr).upper())
    except StopIteration:
        break
#5) print the first 20 even numbers using iterator
itr=iter(range(0,41,2))
while True:
    try:
        print(next(itr))
    except StopIteration:
        break

#generators

#1) Generate an iterator to print even numbers using a generator
def even():
    #generates infinite stream of even numbers
    n=0
    while True :  
        yield n
        n+=2
for i in even():
    #prints even numbers till 20
    print(i)
    if i==20:
        break

#2) Use generator to print the sum of square of fibonacci series
def fibonacci_numbers(nums):
    x, y = 0, 1
    for _ in range(nums):
        x, y = y, x+y
        yield x

def square(nums):
    for num in nums:
        yield num**2

print(sum(square(fibonacci_numbers(10)))) #4895

#3) Print powers of any number upto a given max range using generators
def generator(x,p):
    n=0
    for i in range(p):
        yield x**i
a=generator(3,6)
print(next(a))
for x in a:
    print(x)

#4) use generator expression to calculate the sum of squares of first 10 odd numbers
gen=sum(x*x for x in range(1,20,2))
print(gen) #1330

#5) use generator expression to calculate the product of list1 items wth the all the items of list2 
l1=[1,3,5,7,9]
l2=[0,2,4,6,8]
y=(x*w for x in l1 for w in l2)
print(y) #prints the iterator object
for i in y:
    print(i) #prints the product
