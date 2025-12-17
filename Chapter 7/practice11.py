# Create a program using global keyword to modify a global variable from inside a function.

count = 0  # Global variable
def increment_count():
    global count  # Declare count as global to modify it
    count += 1
    print("Count inside function:", count)
increment_count()
print("Count outside function:", count)
print("Count after another increment:")
increment_count()
print("Count outside function:", count)