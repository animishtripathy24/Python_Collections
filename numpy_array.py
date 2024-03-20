import numpy as np
arr=np.array([1,2,3,49,5],np.int64)
print(arr)

print(arr.dtype)
print(arr.shape)
print(arr.itemsize)

#accessing the first element of the array
print(arr[::-1])

#array support vectorized operation
#i.e if we apply a function it is implemented on each and every element
#of the array
print(arr+2)

# we can also change the array elements in place
arr[3]=4
print(arr)

#array creation methods
# 1.creating an numpy array from a list
arr1=np.array([1,2,23,3,4,5],dtype=np.int64)
print(arr1)

# 2.creating an array from tuple
arr2=np.array((4,5,566,7,8),np.int64)
print(arr2)

# creating a two dimensional array
arr3=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr3)
print(arr3.itemsize)
print(arr3.shape)
print(arr3.size)
print(arr3.dtype)

#creating array from formiter(<iterable sequence>,dtype=<datatype>,[<count>]) function
#dtype is compulsory in this function
# count is the number of element to be read
l=[2,4,6,8,10,12,14,16,18,20]
arr4=np.fromiter(l,dtype=np.int8,count=4)
print(arr4) #output is [2,4,6,8]

#in the case of dictionary it forms the array of keys
d={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
arr5=np.fromiter(d,dtype=np.int8)
print(arr5)

# creating array using arange(start,stop,step,[<dtype>]) function
#by default if no datatype is then it take it as float 
arr6=np.arange(0,100,4,dtype=np.int64)
print(arr6)

#numpy linspace function(<start>,<stop>,<number of elements>) is used to equally divide an array
arr7=np.linspace(1,50,10)
print(arr7)

#creating a two d array
# 1. using array() method
arr7=np.array([[1,2,3],[4,5,6]]);
print(arr7)

# 2. using arange() method
# but here we also have to use reshape method
arr8=np.arange(1,20,2,dtype=np.int32).reshape(5,2)
print(arr8)

# 3.using empty() we can create a 2d array
arr9=np.empty([3,6],dtype=np.int32,order='F')
print(arr9)
#here dtype and order is optional by default the dtype is float and the order is 'C' i.e column wise

# 4. using zeroes() method
#it takes same argument as that of empty function
arr10=np.zeros([3,4],dtype=np.int32,order='F')
print(arr10)

# 5. using ones() method
#same argument as that of empty() function
arr11=np.ones([3,4],dtype=np.int32,order='F')
print(arr11)

#there are three more functions empty_like,ones_like and zeros_like which is used to create array from previously created array
emp_like=np.empty_like(arr4)
print(emp_like) # the dimensions are same as that of the existing array

# if we want to make identity matrix then we use .eye(n,[<dtype>]) function
# it creates two dimensional identity array with n*n size 
identity=np.eye(3,dtype=np.int32)
print(identity)

#if we want to make an array of 3*4 with all the values as 6 then we use .full(<size>,<value i.e to be initialised>)
all=np.full([4,6],5)
print(all)

#if we want to create an array of random integers
# this will generate random float integers from range 0 - 1
random=np.random.rand(3,4)
print(random)

#if we want to generate int type numbers
inti=np.random.rand(5)
print(inti)

# if we want to convert an two dimensional array into one dimensional array then we use .ravel() function
arr12=np.arange(0,100,2).reshape(2,25)
print(arr12)
print(arr12.shape)
arr12=arr12.ravel()
print(arr12)
print(arr12.shape)

#if we want to print three dimensional array
arr13=np.zeros([4,3,2])
print(arr13)



