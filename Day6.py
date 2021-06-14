'''
What is numpy?
NumPy stands for Numerical Python. It is a Python library used for working with arrays. 
It also has functions for working in domain of linear algebra, fourier transform,matrices and routines for shape manipulation.

Why Numpy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
It provides better runtime and space complexity.
It is a very good substitute for MATLAB, OCTAVE, etc as it provides similar functionalities and 
supports with faster development and less mental overhead

Why numpy is faster?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
This behavior is called locality of reference in computer science.
This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

Language in which numpy is written: NumPy is a Python library and is written partially in Python, 
but most of the parts that require fast computation are written in C or C++

limitations of numpy:
1) data type of all the elements in the array is the same
2) Using “nan” in Numpy: “Nan” stands for “not a number”. It was designed to address the problem of missing values. 
NumPy itself supports “nan” but lack of cross-platform support within Python makes it difficult for the user. 
That’s why we may face problems when comparing values within the Python interpreter.
3) Require a contiguous allocation of memory: Insertion and deletion operations become costly as data is stored 
in contiguous memory locations as it requires shifting.

Installation Req:
being Python and pip already installed
pip install numpy

'''

import numpy as np
#creating arrays
x=[1,2,3,4,5]
arr=np.array(x)
print(arr)
type(arr)
print(arr.dtype)   #all the array item are objects of data type object (d-type)

#N-dimensional array examples

a=np.array(0)
print(a.ndim)   #0
a=np.array([1,2,3,4,5,6])
print(a.ndim)   #1
a=np.array({(1,2),(3,4),(5,6)})
print(a.ndim)   #2
a=np.array([[[1,2],[2,3],[3,4]]])
print(a.ndim)   #3
a=np.array([[[[1,2,3,4],[1,2,3,4]]]])
print(a.ndim)  #4
a=np.array({(1,2),(3,4),(5,6)})    
print(a)  #{(1, 2), (3, 4), (5, 6)}
print(a.ndim)  #0
print(type(a)) #<class 'numpy.ndarray'>


#indexing array

a = np.array([1, 2, 3, 4])
print(a[0])     #1
print(a[2] + a[3]) #7

a = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print(a[0, 1])  #2
print(a[-2,-3]) #3

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2]) #6


#slicing an array
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5]) #[2 3 4 5]
print(arr[-3:-1]) #[5 6]
print(arr[1:5:2]) #[2 4]
print(arr[1:]) #[2 3 4 5 6 7]

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4]) #[7 8 9]
print(arr[0:1, 1:4]) #[2 3 4]
print(arr[0:2, 1:4])
'''
[[2 3 4]
 [7 8 9]]
'''
print(arr[..., 1:4]) 
'''
[[2 3 4]
 [7 8 9]]
'''
print(arr[0:1,...]) #[[1 2 3 4 5]]
print(arr[0:2,2]) #[3 8]

#dtype
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)  #[b'1' b'2' b'3' b'4']
print(arr.dtype)    #|S1

arr = np.array([1, 2, 3, 4], dtype='f4')
print(arr)  #[1. 2. 3. 4.]
print(arr.dtype)    #float32

arr = np.array([1, 2, 3, 4], dtype='b')
print(arr)  #[1 2 3 4]
print(arr.dtype)    #int8

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr) #[1 2 3]
print(newarr.dtype) #int32

arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr) #[ True False  True]
print(newarr.dtype) #bool

#copy and view 
'''
The main difference between a copy and a view of an array is 
that the copy is a new array, and the view is just a view of the original array.
'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42
print(arr) #[42 2 3 4 5]
print(x)    #[1 2 3 4 5]
print(x.base) #None

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr) #[42 2 3 4 5]
print(x)    #[42 2 3 4 5]
print(x.base) #[42  2  3  4  5]