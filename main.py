print("Hello world\n")
print(5+8)

# this is single line comment

''' this is multiline comment '''

a=5
b=56.90
c="Animish"

print(type(a))
print(type(b))
print(type(c))

print(c+"2")

d="455"
e=int(float(d))
print(e+2)

f='''Animish
is a good boy''' # triple quotes can also be used to write a string like this
print(f)

g="Animish"
print(g[0])

print(g[1:5]) # it means it starts with index 1 and prints till index 4
# index 5 is excluded


h="   Tripathy    "
print(h)
#if we want to trim the spaces from left side and right side then we use strip() function
print(h.strip())

print(len(h.strip()))

x="ANIMISH"
print(x.lower())
y="tripathy"
print(y.upper())
print(y.replace("pa","xa"))

#to concatenate two strings
var1="My name is "
var2="Animish Tripathy"
print(var1+var2)

#placeholder concept and .format() function
name1="Animish"
name2="Tripathy"
temp="This is a {0} and he is a good boy named {1}".format(name1,name2)
temp1="This is a {1} and he is a good boy named {0}".format(name1,name2)
print(temp)
print(temp1)


print(f"The first student is {name1} and the second student is {name2}");
