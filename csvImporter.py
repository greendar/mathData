from student import *

"""
Need to figure out the format of the CSV files to be loaded in.
Code ==> [0]
Teacher ==> [1]
Mark ==> [2]
Year ==> [3]
Semester ==>[4]
"""

newStudent = Student('Bob', 'Ross')

with open("Book1.csv") as file_in:
    lines = []
    for line in file_in:
        dataList = line.split(",")
        newStudent.addClass = Course(dataList[0], dataList[1], dataList[2], dataList[3], dataList[4])
        #print(newStudent.newCourse)
        #lines.append(line)

newStudent.showStudent()
"""
This is not yet showing the course that have been added
"""

