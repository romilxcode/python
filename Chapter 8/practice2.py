# Write a program to read a text from a given file certificate.txt and find whether it contains the word live.

file= open("Chapter 8/certificate.txt", "r")
dataOffile= file.read()

dataOffile= dataOffile.lower()

if "live" in dataOffile:
    print("Yes Live Word is present in the file")
else:
    print("No Sorry, Live Word is not present in the file") 