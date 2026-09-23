n=int(input("Enter size of list:"))
l=[]
for i in range(n):
    l.append(input("Enter element:"))
print(l)
l.sort()
print(l)
l.reverse()
print(l)