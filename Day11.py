#!/usr/bin/env python
# coding: utf-8

# 
# Matplotlib is one of the most popular Python packages used for data visualization. It is a cross-platform library for making 2D plots from data in arrays. Matplotlib is written in Python and makes use of NumPy, the numerical mathematics extension of Python.
# Matplotlib is an amazing visualization library in Python for 2D plots of arrays.
# Matplotlib is a multi-platform data visualization library built on NumPy arrays and designed to work with the broader SciPy stack. It was introduced by John Hunter in the year 2002.
# One of the greatest benefits of visualization is that it allows us visual access to huge amounts of data in easily digestible visuals.
# Matplotlib consists of several plots like line, bar, scatter, histogram etc.
# matplotlib.pyplot is a collection of command style functions that make Matplotlib work like MATLAB.Pyplot provides functions that interact with the figure i.e. creates a figure, decorates the plot with labels, creates plotting area in a figure.
# fmt: marker|line|color
# marker: '.' – point marker, 'o'- circle, '*'- star, '^'- triangle_up, 'p'- pentagon, 's'- square, '+'-plus, etc. 
# line: '-' (solid line), '--' (Dashed line) , '-.' (Dash dot line) , ':' (Dotted line)
# color: 'b' -blue , 'g'- green , 'r'-red , 'y'- yellow , 'k'- black , 'm'- magenta, 'w'- white, 'c'- cyan

# In[10]:


import matplotlib.pyplot as plt 
x=[1, 2, 3, 4]
y=[1, 4, 9, 16]
plt.plot(x, y) 
plt.axis([0, 6, 0, 20]) 
# Adding the title
plt.title("Simple Plot")
  
# Adding the labels
plt.ylabel("y-axis")
plt.xlabel("x-axis")
plt.show()


# # Figure-
# The matplotlib.figure module contains the Figure class. It is a top-level container for all plot elements. The Figure object is instantiated by calling the figure() function from the pyplot module.

# In[6]:


from matplotlib import figure
import matplotlib.pyplot as plt
fig = plt.figure()
fig


# In[8]:


from matplotlib import figure
import matplotlib.pyplot as plt
fig = plt.figure(figsize=(1,2))
fig


# # Axes-
# Axes class is the most basic and flexible unit for creating sub-plots. A given figure may contain many axes, but a given axes can only be present in one figure. The axes() function creates the axes object.

# In[13]:


import matplotlib.pyplot as plt 
from matplotlib.figure import Figure   
# [left, bottom, width, height]
ax = plt.axes([0, 0, 1, 1])
ax


# In[14]:


# Python program to show pyplot module
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

fig = plt.figure(figsize = (5, 4))
ax = fig.add_axes([1, 1, 1, 1])
ax1 = ax.plot([1, 2, 3, 4], [1, 2, 3, 4])
ax2 = ax.plot([1, 2, 3, 4], [2, 3, 4, 5])

plt.show()


# In[5]:


from matplotlib import pyplot as plt
import numpy as np
import math
x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
ax.plot(x,y)
#setting labels
ax.set_title("sine wave")
ax.set_xlabel('angle')
ax.set_ylabel('sine')
plt.show()


# # Axis:
# This function is used to set some axis properties to the graph.
# parameters:xmin, xmax, ymin, ymax:These parameters can be used to
# set the axis limits on the graph

# In[16]:


import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]
plt.plot(x, y,'or')

# Setting the x-axis to 1-10
# and y-axis to 1-15
plt.axis([0, 10, 1, 15])
plt.show()


# In[17]:


import matplotlib.pyplot as plt

x =[1, 2, 3, 4, 5]
y =[2, 4, 6, 8, 10]
plt.plot(x, y,'or')

# Setting the x-axis to 1-10
# and y-axis to 1-15
plt.axis('off') #turn off the axis
plt.show()


# # Artist:
# Abstract base class for objects that render into a FigureCanvas.
# Typically, all visible elements in a figure are subclasses of Artist.
# 
# Allows full control and fine-tuning of the Matplotlib figure — the top-level container for all plot elements.
# 
# There are two types of Artist objects. The first type is the primitive type, such as a Line2D, Rectangle, Circle, and Text. And the second type is the composite type, such as the Axis, Tick, Axes and Figure.
# It is important to notice that each composite artist may contain other composite artists as well as primitive artists. For example a figure artist can contain an axis artist as well as a rectangle or text artist.

# In[87]:


#A property batch setter. Pass kwargs to set properties.
from matplotlib.artist import Artist
import matplotlib.lines as lines
x=np.arange(0,50)
y=np.sin(x)
fig=plt.figure(figsize=(2,4))
ax=fig.add_axes([1,1,1,1])
ax.plot(x,y)
Artist.set(ax, xlabel ='X-Axis', ylabel ='Y-Axis', title ='Sin graph')
ax2=fig.add_axes([0,1,1,1])
ax2.add_artist(lines.Line2D([0,1],[0,2])) #adding an artist to the figure
ax2.plot()
plt.show()


# # Labels:
# The heading or sub-heading written at the vertical axis (say Y-axis) and the horizontal axis(say X-axis) improves the quality of understanding of plotted stats.

# In[27]:


plt.plot([1,2,3,4,5],[2,3,4,5,6],'*')
plt.xlabel("X-axis")
plt.ylabel('Y-axis')
plt.title('Label Example', loc="left")


# # Legend:
# A legend is an area describing the elements of the graph. In simple terms, it reflects the data displayed in the graph’s Y-axis. It generally appears as the box containing a small sample of each color on the graph and a small description of what this data means.

# In[32]:


x = [3, 1, 3]
y = [3, 2, 1]

plt.plot(x, y)
plt.plot(y,'o', x,'p')

# Adding the legends
plt.legend(["blue", "orange", 'green'])

plt.show()


# # Title:
# the title() method in matplotlib module is used to specify title of the visualization depicted and displays the title using various attributes.

# In[36]:


y = [0,1,2,3,4,5]
x= [0,5,10,15,20,25]
plt.plot(x, y, 'g')
plt.xlabel('x')
plt.ylabel('y')
font1 = {'family':'serif','color':'blue','size':15}
# displaying the title
plt.title("Linear graph", fontdict=font1)

plt.show()


# In[43]:


fig, axes = plt.subplots(1, 3)

# plotting the data in the 1st subplot
axes[0].plot([1, 2, 3, 4], [1, 2, 3, 4])
axes[0].set_title('1st axes', fontstyle='italic')
# plotting the data in the 1st subplot only
axes[0].plot([1, 2, 3, 4], [4, 3, 2, 1])
# plotting the data in the 2nd subplot only
axes[1].plot([1, 2, 3, 4], [4, 3, 2, 1])
axes[1].set_title('2nd axes', fontstyle='normal', fontsize=20)
# plotting the data in the 3rd subplot only
axes[2].plot([1, 2, 3, 4], [1, 1, 1, 1])
axes[2].set_title('3rd axes')


# # Grid:
# The grid() sets the visibility of grids by specifying a boolean value (True/False). We can also choose to display minor or major ticks or both. Also, color, linewidth and linestyle can be changed as additional parameters.

# In[47]:


fig, axes = plt.subplots(1,3, figsize = (12,4))
x = np.arange(1,11)
axes[0].plot(x, x**3, 'g',lw=2)
axes[0].grid(True)
axes[0].set_title('default grid')
axes[1].plot(x, np.exp(x), 'r')
axes[1].grid(color='m', ls = ':', lw = 0.25)
axes[1].set_title('custom grid')
axes[2].plot(x,x)
axes[2].set_title('no grid')
fig.tight_layout()
plt.show()


# # ticks and ticklabels:
# Ticks are the markers denoting data points on the axes and tick labels are the name given to ticks. By default matplotlib itself marks the data points on the axes but it has also provided us with setting their own axes having ticks and tick labels of their choice.

# In[50]:


import math

x = np.arange(0, math.pi*2, 0.05)
y = np.sin(x)
ax = plt.axes()
plt.xlabel("x-axis")
plt.ylabel("y-axis")

plt.plot(x, y, '*k')

# setting ticks for x-axis
ax.set_xticks([0, 2, 4, 6])

# setting ticks for y-axis
ax.set_yticks([-1, 0, 1])

# setting label for y tick
ax.set_yticklabels(["sin(-90deg)", "sin(0deg)", "sin(90deg)"])

plt.show()


# # line plot:
# Line Chart is used to represent a relationship between two data X and Y on a different axis. It is plotted using the pot() function.

# In[65]:


x=np.arange(15)
y= x*x
plt.plot(x,y)
plt.xlabel("Numbers")
plt.ylabel("Squares")
plt.title("Squares of numbers")
plt.legend(['line'], loc="lower right")
plt.show()


# # Bar Plot:
# A bar plot or bar chart is a graph that represents the category of data with rectangular bars with lengths and heights that is proportional to the values which they represent. The bar plots can be plotted horizontally or vertically. A bar chart describes the comparisons between the discrete categories. It can be created using the bar() method.

# In[62]:


x=np.arange(15)
y= x*x
plt.bar(x,y)
plt.title("Bar Chart")
plt.legend(["bar"])
plt.show()


# # Scatter plot:
# Scatter plots are used to observe relationship between variables and uses dots to represent the relationship between them. The scatter() method in the matplotlib library is used to draw a scatter plot.

# In[64]:


x=np.arange(15)
y= x*x
plt.scatter(x,y)
plt.title("Bar Chart")
plt.legend(["scatter"])
plt.show()


# # Pie chart:
# A Pie Chart is a circular statistical plot that can display only one series of data. The area of the chart is the total percentage of the given data. The area of slices of the pie represents the percentage of the parts of the data. The slices of pie are called wedges. The area of the wedge is determined by the length of the arc of the wedge. It can be created using the pie() method.

# In[69]:


x=np.arange(5)
plt.pie(x)
plt.title("Bar Chart")
plt.title("Pie Chart", fontsize=20)
plt.show()


# # Histogram:
# A histogram is basically used to represent data in the form of some groups. It is a type of bar plot where the X-axis represents the bin ranges while the Y-axis gives information about frequency. To create a histogram the first step is to create a bin of the ranges, then distribute the whole range of the values into a series of intervals, and count the values which fall into each of the intervals. Bins are clearly identified as consecutive, non-overlapping intervals of variables. The hist() function is used to compute and create histogram of x.

# In[70]:


fig,ax = plt.subplots(1,1)
a = np.array([22,87,5,43,56,73,55,54,11,20,51,5,79,31,27])
ax.hist(a, bins = [0,25,50,75,100])
ax.set_title("histogram of result")
ax.set_xticks([0,25,50,75,100])
ax.set_xlabel('marks')
ax.set_ylabel('no. of students')
plt.show()


# # Box Plot:
# A box plot which is also known as a whisker plot displays a summary of a set of data containing the minimum, first quartile, median, third quartile, and maximum. In a box plot, we draw a box from the first quartile to the third quartile. A vertical line goes through the box at the median. The whiskers go from each quartile to the minimum or maximum.The data values given to the ax.boxplot() method can be a Numpy array or Python list or Tuple of arrays.

# In[73]:


np.random.seed(10)
a1 = np.random.normal(100, 10, 200)
a2 = np.random.normal(80, 30, 200)
a3 = np.random.normal(90, 20, 200)
a4 = np.random.normal(70, 25, 200)
fig = plt.figure()
# Create an axes instance
ax = fig.add_axes([0,0,1,1])
# Create the boxplot
bp = ax.boxplot([a1,a2,a3,a4])
plt.show()


# # Bubble Plot:
# A bubble plot is very similar to a scatterplot. Using matplotlib library, a bubble plot can be constructed using the scatter() function.To make bubble plot, we need to specify size argument “s” for size of the markers.

# In[78]:


x = np.random.rand(40)
y = np.random.rand(40)
z = np.random.rand(40)
 
# use the scatter function
plt.scatter(x, y, s=z*1000, alpha=0.5)

# show the graph
plt.show()


# # Stack Plot
# Stack Plots are used to visualize multiple linear plots, stacked on top of each other. With a regular line plot, you'd plot the relationship between X and Y. Here, we're plotting multiple Y features on a shared X-axis, one on top of the other.

# In[89]:


# List of 7-days
days = [x for x in range(0, 7)]
Suspected = [12, 18, 35, 50, 72, 90, 100]
Cured = [4, 8, 15, 22, 41, 55, 62]
Deaths = [1, 3, 5, 7, 9, 11, 13]
plt.stackplot(days, Suspected, Cured,
            Deaths, baseline ='zero',colors =['blue', 'orange','brown'])
plt.legend(['suspected','cured', 'deaths'])
plt.title('No of Cases')
plt.xlabel('Day of the week')
plt.ylabel('Overall cases')

plt.show()


# # Contour plot:
# A contour plot is appropriate if you want to see how alue Z changes as a function of two inputs X and Y, such that Z = f(X,Y). A contour line or isoline of a function of two variables is a curve along which the function has a constant value. A contourf() is also available which allows us to draw filled contours.

# In[100]:


x = np.arange(0, 50, 3)
y = np.arange(0, 50, 10)

# Creating 2-D grid of features
[X, Y] = np.meshgrid(x, y)
fig, ax = plt.subplots(1, 1)
Z = (X / 2) + (Y / 4)
# plots contour lines
ax.contourf(X, Y, Z)
ax.set_title('Contour Plot')
ax.set_xlabel('feature_x')
ax.set_ylabel('feature_y')
plt.show()


# # Polar Plot
# The polar() function in pyplot module of matplotlib library is used to make a polar plot.

# In[114]:


x = np.arange(0, 50)
y = np.sin(x*2)
plt.polar(x, y)
plt.title('matplotlib.pyplot.polar() function Example',fontweight ="bold",color="brown")
plt.show()


# In[115]:


# Table Chart


# In[121]:


import matplotlib.pyplot as plt 
   
val1 = ["{:X}".format(i) for i in range(10)] 
val2 = ["{:02X}".format(10 * i) for i in range(10)] 
val3 = [[c for c in range(10)] for r in range(10)] 
   
fig, ax = plt.subplots() 
ax.set_axis_off() 
table = ax.table( 
    cellText = val3,  
    rowLabels = val2,  
    colLabels = val1, 
    rowColours =["palegreen"] * 10,  
    colColours =["palegreen"] * 10, 
    cellLoc ='center',  
    loc ='upper left')         
   
ax.set_title('Table', 
             fontweight ="bold") 
   
plt.show() 


# In[ ]:




