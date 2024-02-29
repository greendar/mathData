class Student:
  def __init__(self, fName, lName):
    self.firstName = fName
    self.lastName = lName
    self.courses = []
  
  def addClass(self, newCourse):
    self.courses.append(newCourse)

  def __str__(self):
    courseList = f"{self.firstName} {self.lastName}"
    for item in self.courses:
      courseList += f'Code: {self.courseCode}    '
      courseList += f'Teacher: {self.courseTeacher}    '
      courseList += f'Mark: {self.courseMark}    '
      courseList += f'Year: {self.schoolYear}    '
      courseList += f'Semester: {self.semester}    '
      return courseList
  


class Course:
  def __init__(self, code, teacher, mark, year, sem):
    self.courseCode = code
    self.courseTeacher = teacher
    self.courseMark = mark
    self.schoolYear = year
    self.semester = sem

  def __str__(self):
    outString = ''
    outString += f'Code: {self.courseCode}    '
    outString += f'Teacher: {self.courseTeacher}    '
    outString += f'Mark: {self.courseMark}    '
    outString += f'Year: {self.schoolYear}    '
    outString += f'Semester: {self.semester}    '
    return outString



if __name__ == "__main__":
  print("i ran")
