'''
NumPy has quite a few useful statistical functions for finding minimum, maximum, percentile standard deviation and variance, etc. from 
the given elements in the array. The functions are explained as follows −

numpy.amin() and numpy.amax()
These functions return the minimum and the maximum from the elements in the given array along the specified axis.

numpy.ptp() -NumPy Peak-to-Peak Function
The numpy.ptp() function returns the range (maximum-minimum) of values along an axis.

numpy.percentile()
Percentile (or a centile) is a measure used in statistics indicating the value below which a given percentage of observations 
in a group of observations fall.

numpy.median()
Median is defined as the value separating the higher half of a data sample from the lower half.

numpy.mean()
Arithmetic mean is the sum of elements along an axis divided by the number of elements. 
The numpy.mean() function returns the arithmetic mean of elements in the array.

numpy.average()
Weighted average is an average resulting from the multiplication of each component by a factor reflecting its importance. 
The numpy.average() function computes the weighted average of elements in an array according to their respective weight given 
in another array. The function can have an axis parameter. If the axis is not specified, the array is flattened.

np.std()- It determines the standard deviation
np.var() – It determines the variance.
'''

import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vgsales.csv')
df.dropna(0, inplace = True)
print(df.to_string())
print(df)

'''
        Rank                                              Name Platform    Year  ... EU_Sales JP_Sales  Other_Sales  Global_Sales
0          1                                        Wii Sports      Wii  2006.0  ...    29.02     3.77         8.46         82.74
1          2                                 Super Mario Bros.      NES  1985.0  ...     3.58     6.81         0.77         40.24
2          3                                    Mario Kart Wii      Wii  2008.0  ...    12.88     3.79         3.31         35.82
3          4                                 Wii Sports Resort      Wii  2009.0  ...    11.01     3.28         2.96         33.00
4          5                          Pokemon Red/Pokemon Blue       GB  1996.0  ...     8.89    10.22         1.00         31.37
...      ...                                               ...      ...     ...  ...      ...      ...          ...           ...
16593  16596                Woody Woodpecker in Crazy Castle 5      GBA  2002.0  ...     0.00     0.00         0.00          0.01
16595  16598  SCORE International Baja 1000: The Official Game      PS2  2008.0  ...     0.00     0.00         0.00          0.01
16596  16599                                        Know How 2       DS  2010.0  ...     0.01     0.00         0.00          0.01
16597  16600                                  Spirits & Spells      GBA  2003.0  ...     0.00     0.00         0.00          0.01

[16598 rows x 11 columns]
'''
jp_sales = df['JP_Sales']
print(jp_sales)
a = np.array(jp_sales.values.tolist())
print(np.amin(a))   #0.0
print(np.amax(a))   #10.22
print(np.mean(a))   #0.077781660441017
print(np.median(a)) #0.0
print(np.std(a))    #0.3092813308359451
print(np.ptp(a))    #10.22
print(np.var(a))    #0.09565494160365334
print(np.average(a))    #0.077781660441017
print(np.percentile(a,75))  #0.04

df2=df[['Other_Sales','Global_Sales']]
print(df2)
a2=np.array(df2)
print(a2)
print(np.amin(a2))   #  0.0
print(np.amax(a2))   #  82.74
print(np.mean(a2))   #  0.2927518375707917
print(np.median(a2)) #  0.05
print(np.std(a2))    #  1.1343004169199336
print(np.ptp(a2))    #  82.74
print(np.var(a2))    #  1.286637435824735
print(np.average(a2))    #  0.2927518375707917
print(np.percentile(a2,75))  #0.2

print(np.amin(a2, axis=1))   #  [8.46 0.77 3.31 ... 0.   0.   0.  ]
print(np.amax(a2, axis=1))   #  [8.274e+01 4.024e+01 3.582e+01 ... 1.000e-02 1.000e-02 1.000e-02]
print(np.mean(a2, axis=1))   #  [4.5600e+01 2.0505e+01 1.9565e+01 ... 5.0000e-03 5.0000e-03 5.0000e-03]
print(np.median(a2, axis=1)) #  [4.5600e+01 2.0505e+01 1.9565e+01 ... 5.0000e-03 5.0000e-03 5.0000e-03]
print(np.std(a2, axis=1))    #  [3.7140e+01 1.9735e+01 1.6255e+01 ... 5.0000e-03 5.0000e-03 5.0000e-03]
print(np.ptp(a2, axis=1))    #  [7.428e+01 3.947e+01 3.251e+01 ... 1.000e-02 1.000e-02 1.000e-02]
print(np.var(a2, axis=1))    #  [1.37937960e+03 3.89470225e+02 2.64225025e+02 ... 2.50000000e-05 2.50000000e-05 2.50000000e-05]
print(np.average(a2, axis=1))    #  [4.5600e+01 2.0505e+01 1.9565e+01 ... 5.0000e-03 5.0000e-03 5.0000e-03]
print(np.percentile(a2,75 ,axis=1))  #  [6.41700e+01 3.03725e+01 2.76925e+01 ... 7.50000e-03 7.50000e-03 7.50000e-03]

print(np.amin(a2, axis=0))   #  [0.   0.01]
print(np.amax(a2, axis=0))   #  [10.57 82.74]
print(np.mean(a2, axis=0))   #  [0.04806302 0.53744066]
print(np.median(a2, axis=0)) #  [0.01 0.17]
print(np.std(a2, axis=0))    #  [0.18858272 1.55498109]
print(np.ptp(a2, axis=0))    #  [10.57 82.73]
print(np.var(a2, axis=0))    #  [0.03556344 2.41796619]
print(np.average(a2, axis=0))    #  [0.04806302 0.53744066]
print(np.percentile(a2,75 ,axis=0))  #  [0.04 0.47]
np.histogram(a2, bins=[0,2,4,6,8,10]) # (array([32325,   566,   156,    60,    26], dtype=int64), array([ 0,  2,  4,  6,  8, 10]))
plt.hist(a2, bins=[0,2,4,6,8,10])       
'''
array([[1.6578e+04, 1.6000e+01, 1.0000e+00, 1.0000e+00, 1.0000e+00],
    [1.5747e+04, 5.5000e+02, 1.5500e+02, 5.9000e+01, 2.5000e+01]]), 
    array([ 0,  2,  4,  6,  8, 10]), <a list of 2 BarContainer objects>)
'''
plt.show()
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
