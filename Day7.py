#Linera Algebra
'''
Reshaping means changing the shape of an array.
The shape of an array is the number of elements in each dimension.
By reshaping we can add or remove dimensions or change number of elements in each dimension and it is returns a view..
Flattening array means converting a multidimensional array into a 1D array.We can use reshape(-1) to do this.
The term broadcasting refers to the ability of NumPy to treat arrays of different shapes during arithmetic operations. 
Arithmetic operations on arrays are usually done on corresponding elements. If two arrays are of exactly the same shape, then these operations are smoothly performed.
'''
import numpy as np

a = np.array([[100,200],[23,12]])  
b = np.array([[10,20],[12,21]])  
print(np.dot(a,b)) 
'''
[[3400 6200]
 [ 374  712]]
'''
print(np.matmul(a,b))
'''
[[3400 6200]
 [ 374  712]]
'''
print(np.vdot(a,b))  #5528
print(np.inner(a,b))  
'''
[[5000 5400]
 [ 470  528]]
'''
print(np.linalg.solve(a,b))  
'''
[[ 0.67058824  1.16470588]
 [-0.28529412 -0.48235294]]
 '''
a=1+2j
b=3+ 4j
print(np.vdot(a,b)) #(11-2j)

a=np.array([1, 2j])
b=np.array([3, 4j])
print(np.vdot(a,b))  #(11+0j)

a = np.array([[100,200],[23,12]])  
b = np.array([[10,20],[12,21]])  
print(np.linalg.det(a)) #-3399.999999999999 
print(np.linalg.inv(b)) 
'''
[[-0.7         0.66666667]
 [ 0.4        -0.33333333]]
'''
print(np.linalg.matrix_rank(b)) #2

#broadcasting shape and reshape

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)  #(2,4)

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]], ndmin=6)
print(arr.shape)  #(1,1,1,1,2,4)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(3, 4)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
newarr = arr.reshape(3, 2,-1)
print(newarr)
print(newarr.shape) #(3,2,2)
print(newarr.base)  #its a view

arr1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
arr2=np.array([1,2,3])
print(np.add(arr1,arr2))

'''
“knowing” that an array’s contents are homogeneous in data type, NumPy is able to delegate the task of performing mathematical 
operations on the array’s contents to optimized, compiled C code. This is a process that is referred to as vectorization. 
The outcome of this can be a tremendous speedup relative to the analogous computation performed in Python, which must painstakingly 
check the data type of every one of the items as it iterates over the arrays, since Python typically works with lists with unrestricted contents.
In the context of high-level languages like Python, Matlab, and R, the term vectorization describes the use of optimized,
pre-compiled code written in a low-level language (e.g. C) to perform mathematical operations over a sequence of data. 
This is done in place of an explicit iteration written in the native language code (e.g. a “for-loop” written in Python).
'''
import numpy as np
import timeit
  
# vectorized sum using IPython
print(np.sum(np.arange(15000)))
  
print("Time taken by vectorized sum : ", end = "")
%timeit np.sum(np.arange(15000))

'''
112492500
Time taken by vectorized sum : 37.2 µs ± 4.16 µs per loop (mean ± std. dev. of 7 runs, 10000 loops each)
'''
#using python sum function
print(sum(range(15000)))
  
print("Time taken by vectorized sum : ", end = "")
%timeit sum(range(15000))
'''
112492500
Time taken by vectorized sum : 426 µs ± 14.5 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)'''
# itersative sum
total = 0
for item in range(0, 15000):
	total += item
a = total
print("\n" + str(a))

print("Time taken by iterative sum : ", end = "")
%timeit a

'''
112492500
Time taken by iterative sum : 45.9 ns ± 3.1 ns per loop (mean ± std. dev. of 7 runs, 10000000 loops each)
'''

#Hence the fastest is numpy.sum() and so vectorised operations are better

'''
NumPy allows the subtraction of two Datetime values, an operation which produces a number with a time unit. Because NumPy doesn’t 
have a physical quantities system in its core, the timedelta64 data type was created to complement datetime64. The arguments for 
timedelta64 are a number, to represent the number of units, and a date/time unit, such as (D)ay, (M)onth, (Y)ear, (h)ours, (m)inutes, 
or (s)econds. The timedelta64 data type also accepts the string “NAT” in place of the number for a “Not A Time” value.
'''
arr=np.arange('2005-02', '2005-03', dtype='datetime64[D]')
print(arr)
'''
['2005-02-01' '2005-02-02' '2005-02-03' '2005-02-04' '2005-02-05'
 '2005-02-06' '2005-02-07' '2005-02-08' '2005-02-09' '2005-02-10'
 '2005-02-11' '2005-02-12' '2005-02-13' '2005-02-14' '2005-02-15'
 '2005-02-16' '2005-02-17' '2005-02-18' '2005-02-19' '2005-02-20'
 '2005-02-21' '2005-02-22' '2005-02-23' '2005-02-24' '2005-02-25'
 '2005-02-26' '2005-02-27' '2005-02-28']
'''
arr=np.array(['2001-01-01T12:00', '2002-02-03T13:56:03'], dtype='datetime64[ms]')
print(arr) #['2001-01-01T12:00:00.000' '2002-02-03T13:56:03.000']

arr=np.array(['2001-01-01T12:00', '2002-02-03T13:56:03.192'], dtype='datetime64')
print(arr) #['2001-01-01T12:00:00.000' '2002-02-03T13:56:03.192']

arr=np.array(['2001-01-01T12:00', '2002-02-03T13:56:03'], dtype='datetime64[D]')
print(arr) #['2001-01-01' '2002-02-03']

print(np.datetime64('nat')) #NaT

print(np.timedelta64(5,'D')) #5 days

print(np.timedelta64(100000,'ms')) #100000 milliseconds

print(np.datetime64('2000')-np.timedelta64(4,'M'))  #1999-09

print(np.timedelta64(82,'s')+np.timedelta64(4,'M'))  #TypeError

print(np.busday_offset('2011-03-20', 0, roll='forward'))  #2011-03-21

print(np.busday_offset('2011-03-20', 3, roll='forward'))  #2011-03-24

print(np.busday_offset('2011-03-20', 6, roll='backward'))  #2011-03-28

print(np.busday_offset('2011-06-25', 2, roll='backward'))  

print(np.is_busday('2011-03-27'))  #False
print(np.is_busday('2011-03-27', weekmask=[0, 0, 0, 0, 0, 1, 1]))  #True

#Boolean Mask
'''
we apply single or multiple conditional operators on array, which returns a boolean array with True for element(s) that passes the 
condition(s) and False for those element(s) that don’t pass the condition(s)
Then we will apply this boolean array to return the actual values from the array. This process is called boolean masking.
'''
arr= np.array([[102, 435, 860, 270, 106],[ 71, 700,  20, 614, 121],[466, 214, 330, 458,  87]])
filter_arr = arr% 2 == 0
print(filter_arr)
'''
[[ True False  True  True  True]
 [False  True  True  True False]
 [ True  True  True  True False]]
'''
print(arr[filter_arr]) #[102 860 270 106 700  20 614 466 214 330 458]
print(np.count_nonzero(np.greater(arr, 200) & np.less(arr, 500))) #6
print(arr[arr >400])  #[435 860 700 614 466 458]
 
