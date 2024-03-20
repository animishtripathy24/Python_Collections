import json
#dictionaries
d={"RSP":"DBMS","SCHAUDHURI":"OS+CD","UPPENDRA":"FLAT"}
print(d)

#if we have to access the keys of the dictionary
print(d.keys())

#if we have to access the values of the dictionary
print(d.values())

#traversing in the dictionary
print("The given dictionary is:")
for i in d :
    print(i+" : "+d[i])
# as dictionary are mutable we can add new key value pair in dictionary
d["PCS"]="Maths"
print(d)

# multiple ways of creating a empty dictionary
employees={}
employees1=dict() # this is dictionary constructor which is used in creating a empty dictionary

#creating a dictionary using dict() constructor
e1=dict(name="Animish",salary="1500000",company="XYZ")
print(e1)

#creating a nested dictionary
f={"Prince":{"Age":17,"Marks":98},"Snehil":{'Age':21,'Marks':99}}
print(f)

#if want all information about prince
print(f["Prince"])

#if we want to access only the age of the prince
print(f["Prince"]["Age"])

#updating the existing value with the dictionary
d["SCHAUDHURI"]="Operating System"
print(d)

#deleting an item from the dictionary
# 1. using del dic[<key>]
del d["SCHAUDHURI"]
print(d)

#pop() method is used to delete an item from the dictionary
#syntax:-pop(<key>,<error message>)
var=d.pop("RSP")
print(f"The value that is deleted is {var}")

print(d.pop("Hazique","Hazique sir is not present there"))
print(d)

#pretty printing of the dictionary using json module and dumps function
#dumps(<dictionary_name>,indent=<n>)
print(json.dumps(d,indent=2))

#checking the existence of the key in the dictionary using membership operator
empl={'salary':10000,'age': 24,'name':"john"}
print("age" in empl)#This will return true
print("John" not in empl)#this will also return true

#various dictionary methods
# 1.len(<dictionary_name>)
var=len(d)
print(f"The length of the dictionary {d} is {var}")

# 2.clear(<dictionary name>)
#it is use to clear all the items in the dictionary
e2=dict(name="Animish",salary="1500000",domain="Data science")
print(f"Before using clear method the dictionary is {e2}")
e2.clear()
print("After using the clear method")
print(e2)

#3. get() method
#this function is used to get an item from the dictionary
e2=dict(name="Animish",salary="1500000",domain="sql")
print(e2.get("domain"))
#we can also pass default message along with the argument
print(e2.get("sal"),"This is not present in the dictionary")





