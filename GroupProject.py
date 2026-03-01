class Course:
    def __init__(self, course_credits, course_code, course_students):
        self.course_credits = course_credits
        self.course_code = course_code  
        self.course_students = course_students

    
    def add_student(self, student):
        self.course_students.append(student)


    def get_students_count(self):
        return len(self.course_students)
    

class Student:
    def __init__(self, student_name, student_id):
        self.student_name = student_name
        self.student_id = student_id


