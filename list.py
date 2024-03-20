lst=[1,2,3,4,5,6,7]
print(lst)
print(type(lst))
print(lst[1])
#list slicing
print(lst[-1:-6:-2])
# lists are mutable datatypes that the python will not create a new list for any changes
print(lst)

#to find the length of the list
print(len(lst))

#append() function is used to add single item at the end of the list
arr=[]
for i in range(1,10,2):
    arr.append(i)

for i in range(len(arr)):
    print(arr[i])
#updating the list
lst[2]=41
print(lst)

#if we have to add multiple items at the end of the list then we use .extend() function
t1=["animish","Kanishk","Pratik"]
t2=["Rahul","Ujjwal"]
print(f"The list 1 is {t1}")
print(f"The list 2 is {t2}")
t1.extend(t2)
print(t1)

#deleting an individual item from the list
del lst[1]
print(lst)

#if we have to insert any item in between the list then we use .index(<pos>,<item>) method
t2.insert(1,"Aman Agarwal")
print(t2)

#if we have to delete an element and returns that deleted element from the list then we use .pop(<index>) method
#this argument(index) is optional
#if no index is specified then it remove the last element from the list
#this pop method raises an exception when trying to delete an element from the empty list
delete=t2.pop()
print(f"The deleted item from the list is {delete}")
print(t2)
t2.pop(0)
print(t2)

#if we want to delete an element based upon the value of that element then we use .remove(<value>) function
#here the argument is essential
#this function doesn't returns anything
t1.remove("Rahul")
print(t1)
# if we have to reverse the items of the list
l1=[3,4,455,7,8,9,9,0]
l1.reverse()
print(l1)
# if we have to count that how many times 9 occured in the list
print(l1.count(9));

#if we have to clear the list items but not the list ten we use .clear() method
l1.clear()
print(l1)

#if we have to sort a list in ascending order
l2=[3,4,5,72,25,6,8,90]
l2.sort()
print(l2)

# if we have to sort the list in descending order
l2.sort(reverse=True)
print(l2)

    
