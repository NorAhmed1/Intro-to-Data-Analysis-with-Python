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





OUTPUT

[1 2 3 4 5]
int64
[ 1.  2.  3.  4.  5.]
1 (5,) 5
[[  1.   2.   3.   4.   5.]
 [  6.   7.   8.   9.  10.]]
float64
2 (2, 5) 10
[[ 0.          0.          0.         ..., -0.         -0.         -0.        ]
 [ 0.25360981  0.24531844  0.22098649 ..., -0.2531162  -0.24083004
  -0.21279677]
 [ 0.49063689  0.4745963   0.42752338 ..., -0.48968194 -0.46591297
  -0.41167944]
 ..., 
 [-0.06236104 -0.06032224 -0.05433917 ...,  0.06223966  0.05921857
   0.05232537]
 [-0.31343844 -0.30319107 -0.27311901 ...,  0.31282838  0.29764381
   0.26299727]
 [-0.54402111 -0.52623521 -0.47404048 ...,  0.54296226  0.51660708
   0.45647263]]
[  0.    2.5   5.    7.5  10. ]
0.0
2.5
5.0
7.5
[[ 0.0863374   0.87005492  0.63508902  0.19288367]
 [ 0.46959526  0.81632689  0.75980748  0.45875954]
 [ 0.21235177  0.28798384  0.21712562  0.89584601]
 [ 0.09919851  0.47632319  0.72275617  0.61975458]
 [ 0.01236602  0.87949186  0.34702253  0.58320134]]
0.0863374002232
0.895846007051
6
[ 5.   7.5]
[ 0.28798384  0.47632319  0.87949186]
[[ 0.28798384]
 [ 0.47632319]
 [ 0.87949186]]
[  0.    2.5   5.    7.5  10. ]
[  0.    2.5   0.    7.5  10. ]
[  0.    2.5   0.    7.5  10. ]
[ 56.    7.5]
[False  True False  True  True]
[  2.5   7.5  10. ]
[[ 0.0863374   1.74010984  1.27017804  0.19288367]
 [ 0.46959526  1.63265379  1.51961495  0.45875954]
 [ 0.21235177  0.28798384  0.21712562  1.79169201]
 [ 0.09919851  0.47632319  1.44551235  1.23950916]
 [ 0.01236602  1.75898372  0.34702253  1.16640267]]
[(1, [2.0, 3.0], 'hey') (2, [3.5, 4.0], 'n')]
(1, [2.0, 3.0], 'hey')
[1 2]
1
1
2015-01-13T12:37:28
2015-01-06
2015-01-01T05
['2016-02-01' '2016-02-02' '2016-02-03' '2016-02-04' '2016-02-05'
 '2016-02-06' '2016-02-07' '2016-02-08' '2016-02-09' '2016-02-10'
 '2016-02-11' '2016-02-12' '2016-02-13' '2016-02-14' '2016-02-15'
 '2016-02-16' '2016-02-17' '2016-02-18' '2016-02-19' '2016-02-20'
 '2016-02-21' '2016-02-22' '2016-02-23' '2016-02-24' '2016-02-25'
 '2016-02-26' '2016-02-27' '2016-02-28' '2016-02-29']
