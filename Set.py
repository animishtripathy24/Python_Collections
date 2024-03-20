#creating a set
s={1,1,1,2,3,2,2,3,3,4,4,4,5,6,6,7,8,8,9}
print(s)
#the result is all the duplicate element are removed and elements are shown in ascending order

#with heterogeneous element types
myset = {"Geeks", "for", 10, 52.7, True}
print(myset)

#the difference between frozen set and normal set is that we can add element in normal set but we cannot add elements in frozen set
s1={1,2,3,4,5,6,7,8,9}
s1.add(11)
print(s1)

#frozen set
s2=frozenset([1,2,3,4,5,6,7])
#s2.add(11)
print(s2)

   
# Python Program to demonstrate union of two sets
 
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}
 
# Union using union() function
population = people.union(vampires)
 
print("Union using union() function")
print(population)
 
# Union using "|" operator
population = people|dracula
 
print("\nUnion using '|' operator")
print(population)



# Python program to demonstrate intersection
# of two sets

set1 = set()
set2 = set()

for i in range(5):
	set1.add(i)

for i in range(3,9):
	set2.add(i)

# Intersection using
# intersection() function
set3 = set1.intersection(set2)

print("Intersection using intersection() function")
print(set3)

# Intersection using "&" operator
set3 = set1 & set2

print("\nIntersection using '&' operator")
print(set3)


#python sets can be cleared using clear() function
s4={1,2,3,4,5,6,7,8,9,0}
print(s4)
s4.clear()
print(s4)
# if we want to add multiple elementswe use update method
#in update method we can pass list or a tuple or a set itself
s6={1,2,3,5,6,7}
s6.update({1,8,9,10,12})
print(s6)
#to get the length of the set
print(len(s6))
#if we want to remove any item from the set then we use .remove() method
s6.remove(5)
print(s6)
#if we pass an item which is not present in the set then the remove function will show error
#to avoid this type of error we simply use .discard(<item>)
#if the element is present in the set it simply removes it otherwise no error will occur
s6.discard(13)
print(s6)
#.pop() it takes no argument and removes the element from the front
var=s6.pop()
print(f"the element which is deleted is {var} and the set is {s6}")
#.clear() method clears the set
s6.clear()
print(s6)
s7={1,8,9,10,12}
print(s7)
