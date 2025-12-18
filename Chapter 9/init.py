class Student:
    schoolName= "ABC School"

    def __init__(self, name, course):
        self.name= name
        self.course= course

        print(self.name)
        print(self.course)

student1= Student("Romil", "Bca") # init method will be called
print("Student1 Name-", student1.name)
print("Student1 Course-", student1.course)

student2= Student("Ankit", "BTech")
print("student2 Name-", student2.name)
print("student2 Course-", student2.course)
