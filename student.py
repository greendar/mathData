class Student:
  def __init__(self, fName, lName):
    firstName = fName
    lastName = lName
    courses = []
  
  def addClass(self, newCourse):
    self.courses.append(newCourse)


class Course:
  def __init__(self, code, teacher, mark, year, sem):
    courseCode = code
    courseTeacher = teacher
    courseMark = mark
    schoolYear = year
    semester = sem

if __name__ == "__main__":
  print("i ran")
