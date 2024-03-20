import json

n=int(input("Enter the size of the list"))
l=[]
for i in range(n):
      c=int(input())
      l.append(c)
d={}
for item in l:
      key=item
      if key not in d:
          count=l.count(key)
          d[key]=count
print(f"The list is {l}")
print("The frequency of the items are:")
print(json.dumps(d,indent=2))
