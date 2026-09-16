def obt_marks(a,b,c):
    return a + b + c
a=int(input("Enter marks of subject 1: "))
b=int(input("Enter marks of subject 2: "))
c=int(input("Enter marks of subject 3: "))
obt=obt_marks(a,b,c)
def percentage(marks=150, obt=obt):
    print("Total marks:", marks)
    print("Obtained marks:", obt)
    print("Percentage:", (obt / marks) * 100)
    return (obt / marks) * 100
percentage()