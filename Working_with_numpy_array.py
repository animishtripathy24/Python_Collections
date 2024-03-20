import numpy as np
x=[[1,2,3],[4,5,6],[7,8,9]]
arr=np.array(x,dtype=np.int32)
print(arr)

#finding the sum across columns
print(arr.sum(axis=0))

#finding the sum across rows
print(arr.sum(axis=1))

#finding the transpose of the array
print(arr.T)

#printing the each and every element of the array
(a,b)=arr.shape
for i in range(a):
    for j in range(b):
        print(arr[i][j])

# another way of printing elements of the array
# arr.flat returns the iterator of every element of the array
for item in arr.flat:
    print(item)

#ndim returns the numbetr of dimension of the array
print(arr.ndim)

#to get the number of the elements we use size
print(arr.size)

#to get the total number of bytes consumed by my array we use nbytes
print(arr.nbytes)

# to get the index of the maximum element of the array
one=np.array([21,92,83,44,51,67])
var=one.argmax()
print(var)

# to get the index of the minimum element of the array
one=np.array([21,92,83,44,51,67])
var1=one.argmin()
print(var1)

#to get the sorted sequence of the array
one=np.array([21,92,83,44,51,67])
var2=one.argsort()
print(var2)

#to get the maximum element of the two dimensional array
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var3=two.argmax()
print(var3)

#if we want maximum element along axis=0
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var4=two.argmax(axis=0)
print(var4)

#if we want maximum element along axis=1
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var5=two.argmax(axis=1)
print(var5)

#if we want minimum element along axis=0
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var6=two.argmin(axis=0)
print(var6)

#if we want minimum element along axis=1
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var7=two.argmin(axis=1)
print(var7)

#if we want the sorted sequence
two=np.array([[1,2,3],[4,5,6],[7,8,9]])
var8=two.argsort(axis=0)
print(var8)

ar1=np.array([[1,2,3],[4,5,6],[7,8,9]])
ar2=np.array([[1,4,6],[7,2,9],[2,5,3]])
print(ar1+ar2)
print(ar1*ar2)

#to perform the square root of each and every element of the numpy array
# we use sqrt() function
print(np.sqrt(one))

#we can also use max and min sum
print(ar1.max())
print(ar1.min())
print(ar1.sum())

#to find any element in the array
var9=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(np.where(arr>6))

#to count the non_zero elements in the array
print(f"The number of non zero elements in the array is {np.count_nonzero(var9)}")

# if we want to convert an array into list then we use tolist() method
print(var9.tolist())

# if we want to sort the array
var10=np.array([2160,97,83,48,589,67])
print(np.sort(var10,axis=None))

#if we want to sort the two dimensional array
a = np.array([[1,4],[3,1]])
print(f"The array to be sorted is {a}")
print(np.sort(a))
print(np.sort(a,axis=0))
print(np.sort(a,axis=1))

# if we want to horizontally divide the array into equal parts
a3=np.arange(24).reshape(4,6)
print(a3)
a,b=np.hsplit(a3,2)
print(a)
print(b)

#if we want to divide it vertically then we have to use vsplit(<array_name>,<number of equal parts>) method
a4=np.arange(24).reshape(4,6)
print(a4)
c,d=np.vsplit(a4,2)
print(c)
print(d)

#if we want to divide it into unequal parts
#then we use split() function
j,k,l=np.split(a4,[2,4],axis=1)
print(j)
print(k)
print(l)

