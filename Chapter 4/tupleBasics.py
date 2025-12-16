#tuple basics

myTuple= (78, 90, 75)
studentTuple= ("Romil", "Khushi", "Divya", "Isha", "Divya")

#studentTuple[1] is immutable it means it can not be changed after creating it.

print(studentTuple[2])

#empty tuples

emptyTuple= ()
singleTuple= (1,)
print(type(emptyTuple))
# print(type(studentTuple))
print(type(singleTuple))
print(studentTuple.index("Divya"))
print(studentTuple.count("Divya"))
