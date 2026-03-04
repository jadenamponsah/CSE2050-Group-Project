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
    def __init__(self, student_name, student_id, student_courses):
        self.student_name = student_name
        self.student_id = student_id
        self.student_courses = student_courses

    def enroll_course(self, course, course_grade):
        self.student_courses.append((course, course_grade))

    def update_grade(self, course, course_grade):
        """modify the grade of a course for a student"""
        for i in range(len(self.student_courses)):
            if self.student_courses[i][0] == course:
                self.student_courses[i] = (course, course_grade)
                break

    def calculate_gpa(self):
        """calculate the GPA of a student based on their courses and grades"""
        total_credits = 0
        total_points = 0
        for course, grade in self.student_courses:
            total_credits += course.course_credits
            total_points += course.course_credits * grade
        if total_credits == 0:
            return 0
        return total_points / total_credits
    

    def get_courses(self):
        """return a list of courses the student is enrolled in"""
        return [course for course, grade in self.student_courses]
    

    def get_course_info(self):
        """return a list of tuples containing course code and grade for each course the student is enrolled in"""
        return [(course.course_code, grade) for course, grade in self.student_courses]

        
class University:
    def __init__(self, university_name, university_courses, university_students):
        self.university_name = university_name
        self.university_courses = university_courses
        self.university_students = university_students

                    
    def add_course(self, course_code, course_credits):
        """if the course does not exist, create and store it; return the course object."""
        for course in self.university_courses:
            if course.course_code == course_code:
                return course
        new_course = Course(course_credits, course_code, [])
        self.university_courses.append(new_course)
        return new_course
        
    
    def add_student(self, student_name, student_id):
        """if the student does not exist, create and store it; return the student object."""
        for student in self.university_students:
            if student.student_id == student_id:
                return student
        new_student = Student(student_name, student_id, [])
        self.university_students.append(new_student)
        return new_student
    
    def get_student(self, student_id):
        """return the student object with the given student_id, or None if not found."""
        for student in self.university_students:
            if student.student_id == student_id:
                return student
        return None
    

    def get_course(self, course_code):
        """return the course object with the given course_code, or None if not found."""
        for course in self.university_courses:
            if course.course_code == course_code:
                return course
        return None
    
    def course_enrollment(self, course_code):
        """return a list of student names enrolled in the course with the given course_code."""
        course = self.get_course(course_code)
        if course is None:
            return []
        return [student.student_name for student in course.course_students]
    
    def get_students_in_course(self, course_code):
        """return a list of student objects enrolled in the course with the given course_code."""
        course = self.get_course(course_code)
        if course is None:
            return []
        return course.course_students
    
import unittest

class TestUniversitySystem(unittest.TestCase):

    def test_course_creation(self):
        course = Course(3, "CS101", [])
        self.assertEqual(course.course_code, "CS101")
        self.assertEqual(course.course_credits, 3)
        self.assertEqual(course.get_students_count(), 0)

    def test_add_student_to_course(self):
        course = Course(3, "CS101", [])
        student = Student("Alice", 1, [])
        course.add_student(student)
        self.assertEqual(course.get_students_count(), 1)

    def test_student_enroll(self):
        course = Course(3, "CS101", [])
        student = Student("Alice", 1, [])
        student.enroll_course(course, 4.0)
        self.assertEqual(len(student.get_courses()), 1)

    def test_gpa_calculation(self):
        course = Course(3, "CS101", [])
        student = Student("Alice", 1, [])
        student.enroll_course(course, 4.0)
        self.assertEqual(student.calculate_gpa(), 4.0)

    def test_add_course_to_university(self):
        uni = University("TestUni", [], [])
        course = uni.add_course("CS101", 3)
        self.assertEqual(uni.get_course("CS101"), course)
        

    def test_duplicate_course(self):
        uni = University("TestUni", [], [])
        course1 = uni.add_course("CS101", 3)
        course2 = uni.add_course("CS101", 3)
        self.assertEqual(course1, course2)

    def test_get_nonexistent_student(self):
        uni = University("TestUni", [], [])
        self.assertIsNone(uni.get_student(999))


if __name__ == "__main__":
    unittest.main()
