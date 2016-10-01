import numpy as np
import matplotlib.pyplot as pp

a = np.array([1,2,3,4,5])
print(a)
print(a.dtype)

a = np.array([1,2,3,4,5], dtype=np.float64)
print(a)
print(a.ndim, a.shape, a.size)

b = np.array([[1,2,3,4,5],[6,7,8,9,10]], dtype=np.float64)
print (b)
print (b.dtype)
print(b.ndim, b.shape,b.size)

np.zeros((3,3),'d')
    # string 'd' is a shorthand for the float64 dtype, it stands for double
np.empty((4,4),'d')
    # this will just use a regional memory as it is, so we may get nonsensical values
np.linspace(0, 5, 10)
    # chooses 5 elements between 0 and 10
np.arange(0,10,2)
    # chooses the step distance between 2 elements. Says: Increase by 2, go between 0 and 10
np.random.standard_normal((2,4))



a = np.random.standard_normal((2,4))
b = np.random.standard_normal((2,4))

np.vstack([a,b])
    # this combines the two arrays and gives you 4 rows and 3 columns
np.hstack([a,b])
    # this gives you an array with 2 rows and 6 columns
a.transpose()

np.save('example.npy',a)
    # this saves array "a" as the name 'example.npy'


x = np.linspace(0,10,40)
sinx = np.sin(x)

pp.plot(x,sinx)

cosx = np.cos(x)

pp.plot(x,sinx,'x')
pp.plot(x,cosx,'o')


y = sinx * cosx
z = cosx**2 - sinx**2

pp.plot(x,y)
pp.plot(x,z)
pp.legend(['sin(x) cos(x)', 'cos(x)^2 - sin(x)^2'])


np.dot(sinx,cosx)
    # treats the values as vectors

mat_outer = np.outer(sinx,cosx)
    # this takes the outer product , which builds every possible combination of the elements from the two vectors
print(mat_outer)


"""
v = np.space(0,10,5)
print (v + 1)

vv = np.outer(v,v)
    # adding a one-dimensional array to a two-dimensional array
print (vv + v)
    # the result is a two-dimensional array where the one-dimensional array has been added to every row
    
# if we wanted to instead add it to every column, we'd first have to turn it into a proper n-by-one column vector, by adding a dimensino with numpy newaxis
vv + v[:,np.newaxis]

"""


# INDEXING AND SLICING NUMPY ARRAYS



v = np.linspace(0,10,5)
print (v)
print (v[0])
print (v[1])
print (v[2])
print (v[3])

vv = np.random.random((5,4))
print (vv)
print (vv[0,0])
    # the first index refers to the row, the second the column
print (vv[2,3])
    # this is diff than what we can do with lists
    # with lists, this command would have to be written as follows:
list_array = [[1,2,3],[4,5,6],[7,8,9]]
print (list_array[1][2])


# SLICING
print (v[2:4])
    # for one-dimensional arrays
print (vv[2:5,1])
    # for two-dimensional arrays
print (vv[2:5,1:2])

# with slicing, if you create a new arrasy by slicing and modifying its values, you end up modifying the original array
print (v)
v2 = v[2:4]
v2[0] = 0
print (v)

# to do this without it changing, make a copy:
v3 = v[2:4].copy()
v3[0] = 56
print (v)
print (v3)


print (v > 0)
bool_index = v > 0
print (v[bool_index])

#Ex. you only want to operate on the elements in vv that are greater than 5

vv[vv > 0.5] = vv[vv > 0.5] * 2
print (vv)



# RECORDS AND DATES

reca = np.array([(1,(2.0,3.0),'hey'),(2,(3.5,4.0),'n')],
                dtype=[('x',np.int32),('y',np.float64,2),('z',np.str,4)])
print (reca)
print (reca[0])
print (reca['x'])
print (reca['x'][0])
print (reca[0]['x'])


np.datetime64('2015')
print (np.datetime64('2015-01-13 12:37:28'))

# can mathematically operate on dates:
print (np.datetime64('2015-01-01') + np.timedelta64(5,'D'))
print (np.datetime64('2015-01-01') + np.timedelta64(5,'h'))

np.datetime64('2015-01-01').astype(float)
    # this tells us the number of days from a standard date, the beginning of 1970
np.datetime64('1970-01-01').astype(float)

# datetime objects are recognized throughout numpy, so you can build ranges of dates (as shown below)
r = np.arange(np.datetime64('2016-02-01'),np.datetime64('2016-03-01'))
print (r)
