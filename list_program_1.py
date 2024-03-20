# at first we have to take input in the list
l1=eval(input("Enter the list"))
s=0
for i in range(0,10,2):
    s=s+l1[i]
print(f"The sum of alternate member of the list : {s}")

#secondly we have to find the mean of the numbers
l2=eval(input("Enter the list"))
length=len(l2)
s1=0
for i in range(0,10,4):
    s=s+l2[i]
m=s/length
print(f"The mean of the given list is {m}")
