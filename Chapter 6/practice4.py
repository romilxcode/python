# Write a program that prints the sum of first n natural numbers.
# For example, if n = 5, the output should be 15 (1+2+3+4+5)

n= int(input("Enter a number: "))
sum= 0

while n>=1:
    sum= sum+n
    n= n-1

print("Sum= ", sum)
print("n= ", n)