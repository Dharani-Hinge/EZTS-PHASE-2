students_grade=[]
students_grade.append((1,"Srinidhi"))
students_grade.append((2,"Preethi"))
students_grade.append((3,"Mithra"))
students_grade.append((4,"Madhu"))
students_grade.sort(reverse=True)
print("Priority wise sorted")
print(students_grade)
print("Original queue")
while students_grade:
    print(students_grade.pop())