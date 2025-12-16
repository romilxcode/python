#Dictionary Basics

student= {
    "name": "Romil Unadkat",
    "city": "Amreli",
    "age": 27,
    "rollNumber": 69,
}

print(type(student))
print(student["name"])
print(student)
print(student["city"])
# student["city"]= "Bengaluru"
# print(student)
student["favSubject"]= "Python"
print(student)
student.pop("favSubject")
print(student)
print(student.keys())
print(student.values())
print(student.items())