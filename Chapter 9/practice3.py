# Create a class Student that take 3 marks and has a method average()

class Student:
    def __init__(self, name, listOfMarks):
        self.name = name
        self.listOfMarks = listOfMarks

    def average(self):
        total = 0
        for eachValue in self.listOfMarks:
            total = total + eachValue

        average = total / 3
        print("Average is: ", average)
        print(self.name)
        return average

student1= Student("Romil", [90, 98, 88])
print("Average Marks: ", student1.average())
