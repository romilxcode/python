# Write a program with a local variable score inside a function and global one outside.

score = 100  # Global variable
def display_scores():
    score = 50  # Local variable
    print("Local score:", score)
    print("Global score:", globals()['score'])
display_scores()
print("Global score outside function:", score)