a=int(input("Enter the number of elements:"))
d={}
for i in range(a):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
print(d)
b=input("Enter key to search:")
if b in d:
    print("Value:", d[b])
else:
    print("Key not found.") 
c=input("Enter key to delete:")
if c in d:
    del d[c]
    print("Key deleted.")
else:
    print("Key not found.")
f=input("Enter key to update:")
if f in d:
    new_value=input("Enter new value:")
    d[f]=new_value
    print("Key updated.")
e=input("Enter key to insert:")
if e not in d:
    new_value=input("Enter value:")
    d[e]=new_value
    print("Key inserted.")
else:
    print("Key already exists.")
print("Final dictionary:", d)