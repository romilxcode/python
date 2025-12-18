# file = open("report.txt", "r")
# data= file.read()
# print("File Data is:\n ", data)
# file.close() 

# with open("report.txt", "r") as f:
#     data= f.read()
#     print("File Data", data)

with open("Chapter 8/newTextFile.txt", "r") as f:

#     line1= f.readline()
#     line2= f.readline()
#     line3= f.readline()
#     line4= f.readline()
#     line5= f.readline()
#     line6= f.readline()

#     print("Line 1", line1)
#     print("Line 2", line2)
#     print("Line 3", line3)
#     print("Line 4", line4)
#     print("Line 5", line5)
#     print("Line 6", line6)
    readLinesMethod= f.readlines()
    print(readLinesMethod)