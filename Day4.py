# classes and objects
#1) create a program to compute sum and product of two numbers using classes

class Calculate:
    result ="Your answer is:"
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    
    def add(self):
        return self.n1+self.n2

    def product(self):
        return self.n1*self.n2
    
ob = Calculate(2, 10)

print(ob.result, ob.add())
print(ob.result, ob.product())

#2) create a program to compute sum and product of two numbers using polymorphism in classes

class Addition:
    result ="Your sum is:"
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2
    
    def cal(self):
        return self.n1+self.n2

class Product:
    result ="Your product is:"
    def __init__(self,n1,n2):
        self.n1 = n1
        self.n2 = n2

    def cal(self):
        return self.n1*self.n2
    
ob1 = Addition(2, 10)
ob2=Product(4,5)
def compute(var):   #Polymorphic function 
    print(var.result, var.cal())
    
compute(ob1)
compute(ob2)

#3) Present the idea of encapsulation in classes
class Computer:

    def __init__(self):
        self.__maxprice = 900 #private attribute can't be changed outside the class

    def sell(self):
        print("Selling Price: {}".format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell()

# change the price
c.__maxprice = 1000
c.sell()

# using setter function
c.setMaxPrice(1000)
c.sell()

#4) Present the idea of inheritance in classes
class Compute:
    result ="Your sum is:"
    def __init__(self):
        print('Parent Class')
    def res(self):
        print(self.result)
    def disp(self):
        print("Calculate")
        

class Sum(Compute):
    def __init__(self,n1,n2):
        super().__init__()
        self.n1 = n1
        self.n2 = n2
        print('Child Class')

    def cal(self):
        return self.n1+self.n2

    def res(self, result): #overridden method
        super().res()
        print(result)

ob = Sum(5,10)
x=ob.cal()
ob.res(x)
ob.disp()

#5)Write a class to find all pair of elements from a given array whose sum equals a specific target number.
class Find:
   def sum(self, target, *nums):
        for i in nums: 
            for j in nums:
                if i+j == target:
                    print('(',i,',',j,')')

obj=Find()
obj.sum(40,10,20,10,40,30,60,70)

#Closure and decorators

#1) Using closures print the nonlocal variable outside the scope of variable
def num(x):
    def nums():
        return x
    return nums
x=num(2)
print("Sum of 2 and 5 is:",x()) #2


#2) Using closures print the sum of two numbers
def num1(x):
    def num2(y):
        return x+y
    return num2
sum2=num1(2)
sum4=num1(4)
print("Sum of 2 and 5 is:",sum2(5))
print("Sum of 4 and 5 is:",sum4(5))
print("Sum of 2, 4 and 6 is:",sum2(sum4(6)))

#3) Use Decorators to check if the input number is positive or not
def positive_num(fun):
    def check(y):
        if y>0:
            return fun(y)
        else:
            print("Not a positive number")
    return check
    
@positive_num
def num(y):
    print(y)

num(4)
num(-2)

#4) Write the above code without using @
def positive_num(fun):
    def check(y):
        if y>0:
            return fun(y)
        else:
            print("Not a positive number")
    return check
    
def num(y):
    print(y)

num=positive_num(num)

num(4)
num(-2)

'''
5) Print this pattern using decorators
******************************
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
Hello
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
******************************
'''

def stars(func):
    def star():
        print('*' * 30)
        func()
        print('*' * 30)
    return star

def modulo(func):
    def mod():
        print('%' * 30)
        func()
        print('%'*30)
    return mod

@stars
@modulo
def string():
    print("Hello")

string()


# Descriptors
# Creating Descriptors using classes
class Descriptor(object):

	def __init__(self, name =''):
		self.name = name

	def __get__(self, obj, objtype):
		return self.name + " Tayal"

	def __set__(self, obj, name):
		if isinstance(name, str):
			self.name = name
		else:
			raise TypeError("Name should be string")
		
class Des(object):
	name = Descriptor()
	
ob = Des()
ob.name = "Nancy"
print(ob.name) # Nancy Tayal

# Creating Descriptors using property() function

# Python program to explain property() function
	
# Alphabet class
class Alpha:
	def __init__(self, value):
		self._value = value
			
	# getting the values
	def getValue(self):
		print('Getting value')
		return self._value
			
	# setting the values
	def setValue(self, value):
		print('Setting value to ' + value)
		self._value = value
			
	# deleting the values
	def delValue(self):
		print('Deleting value')
		del self._value
		
	value = property(getValue, setValue, delValue, )
	
# passing the value
x = Alpha('Nancy')
print(x.value)
	
x.value = 'Nancy Tayal'
	
del x.value

# Creating Descriptors using @property decorator
class Alpha:
	def __init__(self, value):
		self._value = value
			
	# getting the values	
	@property
	def value(self):
		print('Getting value')
		return self._value
			
	# setting the values	
	@value.setter
	def value(self, value):
		print('Setting value to ' + value)
		self._value = value
			
	# deleting the values
	@value.deleter
	def value(self):
		print('Deleting value')
		del self._value
	
	
# passing the value
x = Alpha('Nancy')
print(x.value)
	
x.value = 'Nancy Tayal'
	
del x.value

