"Positional Arguments"
def display(name, age):
    print(f"Name: {name}, Age: {age}")
display("Alice", 30)

"Default Arguments"
def display(name, age=25):
    print(f"Name: {name}, Age: {age}")
display("Bob")  # Uses default age

"Keyword Arguments"
display(name="Charlie", age=35)
display(age=40, name="David") # Order doesn't matter with keyword arguments

"Arbitrary Arguments"
def display(*args):
    for arg in args:
        print(arg)
display("Alice", 30)
display("Bob", 25, "Engineer")

"Arbitrary Keyword Arguments"
def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")
display(name="Charlie", age=35)
display(city="New York", country="USA")