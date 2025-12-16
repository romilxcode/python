# Write a program to print all even numbers between 1 and 50 using a while loop.

#even number = 2, 4, 6, 8....
#odd number = 1, 3, 5, 7....

num= 1

while (num<=50):
    if(num%2 ==0):
        print(num)
    num= num+1

print("You are out of the loop now...")