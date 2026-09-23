n=int(input("Enter number of elements:"))
t=()
for i in range(n):
    t+=(input("Enter element:"),)
print(t)
a=int(input("Enter index to search:"))
if 0 <= a < len(t):
    print("Element found at index", a, ":", t[a])
else:
    print("Element not found")