#Write a program to check grade based on marks(A/B/C/D) using if-elif-else.

marks = int(input("Enter your marks: "))
if marks >= 90:
    grade = 'A'
    print(grade)
elif marks >= 80:
    grade = 'B'
    print(grade)
elif marks >= 70:
    grade = 'C'
    print(grade)
elif marks >= 60:
    grade = 'D'
    print(grade)
else:
    print("Sorry, dear student, you have failed, better luck next time!")