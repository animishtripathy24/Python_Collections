import pandas as  pd
import numpy as np

d={"A" : 1,"B" : 2,"C" : 3,"D" : 4}
s1=pd.Series(d);
print(f"The Series is : \n{s1}")
#extracting the slices from the series object
print(s1[0:4:2])
#modifying the elements of the series object
s1[2:]=90
print(f"After modifying the series object")
print(s1)

#Renaming index
s1.index=["P","Q","R","S"]
print(f"After renaming the series looks like:\n {s1}")

#inorder to to get the first five rows of the series we use .head() function
print(s1.head())

#.tail() function returns the last five rows of the series object
print(s1.tail())

#vectorised operation in series
a=np.arange(11,31,2)
s2=pd.Series(a)
print(s2)
print(s2+2)

#filtering series object
print(s2>20) #return boolean series for matching returns true and for non matching returns false

#sorting series values
b=np.array([2,6,1,4,9,13])
s3=pd.Series(data=b)
print(f"After sorting the series looks likes {s3.sort_values()}")
#by default it sort in ascending order
#if we have to sort in descending order
print(f"After sorting the series looks likes {s3.sort_values(ascending=False)}")

