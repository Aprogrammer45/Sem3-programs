num=int(input("Enter a number: "))
i=1
total=0
while i<=10:
    result=num*i
    print(f"{num} x {i} = {result}")
    total+=result
    i+=1    
print(f"Total: {total}")