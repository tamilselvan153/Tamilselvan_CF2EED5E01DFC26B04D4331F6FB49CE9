'''
Implement a function  called sort_students that takes a list of Student objects as input and Sorts the 
list based on their CGPA (Cumulative Grade Point Average ) in descending order. Each student object
has the following  attributes: name (string),roll_number (string), and cgpa (float).Test the function 
with different input lists of  Students. 
'''

class Student:

  def __init__(self,name,roll_number,cgpa):
    self.name = name 
    self.roll_number =roll_number 
    self.cgpa = cgpa


def sort_students(Student_list):
  # Sort the list of Student in descending order of CGPA
  sorted_students = sorted (Student_list,
       key=lambda student: student.cgpa,
      reverse=True)
# Syntax - lambda arg:exp
  return sorted_students



# Example usage:
Students= [
    Student("Prithis","A123", 7.8),
  Student("Krishnan","A124",8.9),
Student("Vijayraj","A125",9.1),
Student("Sriram","A126",9.9),
]

sorted_students =sort_students(Students)

# Print the Sorted list of Students
for student in sorted_students:
  print("Name:{},Roll Number:{},CGPA:{}".format(student.name,
                              student.roll_number,
           student.cgpa))