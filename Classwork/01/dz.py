try:
    fin = open('./Classroom/Exception_File/students.txt','r')
    students = fin.readlines()
    marks = []
    for student in students:
        tmp = student.split()
        marks.append(float(tmp[2]))
    print(marks)
    
except:
    print("ups")
finally:
    pass