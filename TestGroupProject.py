import unittest
from GroupProject import Course, Student, University

class TestCourse(unittest.TestCase):

    """Checks that a course is created with the correct code and credits - Karsten"""
    def test_create_course(self):
        course = Course(3, "CSE1010", [])

        self.assertEqual(course.course_code, "CSE1010")
        self.assertEqual(course.course_credits, 3)

    """Makes sure a student can be added to a course correctly - Karsten"""
    def test_add_student(self):
        course = Course(3, "CSE1010", [])
        student = Student("Karsten", 1, [])

        course.add_student(student)
        self.assertEqual(course.get_students_count(), 1)

    """Checks that the total number of students in a course is counted correctly - Karsten"""
    def test_students_count(self):
        course = Course(3, "CSE1010", [])

        student1 = Student("Karsten", 1, [])
        student2 = Student("Jaden", 2, [])
        student3 = Student("Michael Jordan", 3, [])

        course.add_student(student1)
        course.add_student(student2)
        course.add_student(student3)
        self.assertEqual(course.get_students_count(), 3)

class TestStudent(unittest.TestCase):

    """Checks that a student can enroll in a course successfully - Karsten"""
    def test_enroll_course(self):
        course = Course(3, "CSE1010", [])
        student = Student("Karsten", 1, [])
        student.enroll_course(course, 4.0)

        self.assertEqual(len(student.get_courses()), 1)

    """Makes sure a student's grade can be updated correctly - Karsten"""
    def test_update_grade(self):
        course = Course(3, "CSE1010", [])
        student = Student("Karsten", 1, [])

        student.enroll_course(course, 3.0)
        student.update_grade(course, 4.0)

        info = student.get_course_info()
        self.assertEqual(info[0][1], 4.0)

    """Checks that GPA is calculated correctly when multiple courses are taken - Karsten"""
    def test_calculate_gpa(self):
        course1 = Course(3, "CSE1010", [])
        course2 = Course(3, "MATH1010", [])

        student = Student("Karsten", 1, [])
        student.enroll_course(course1, 4.0)
        student.enroll_course(course2, 2.0)
        gpa = student.calculate_gpa()

        self.assertEqual(gpa, 3.0)

    """Makes sure GPA is 0 when the student has no courses - Karsten"""
    def test_gpa_empty(self):
        student = Student("Karsten", 1, [])
        self.assertEqual(student.calculate_gpa(), 0)

    """Checks that all enrolled courses are returned correctly - Karsten"""
    def test_get_courses(self):
        student = Student("Karsten", 1, [])
        course1 = Course(3, "CSE1010", [])
        course2 = Course(3, "MATH1010", [])
        course3 = Course(3, "PHYS1010", [])

        student.enroll_course(course1, 4.0)
        student.enroll_course(course2, 4.0)
        student.enroll_course(course3, 4.0)

        courses = student.get_courses()
        self.assertEqual(len(courses), 3)


class TestUniversity(unittest.TestCase):

    """Checks that a course can be added to the university - Karsten"""
    def test_add_course(self):
        uni = University("UConn", [], [])
        course = uni.add_course("CSE1010", 3)
        self.assertEqual(uni.get_course("CSE1010"), course)

    """Makes sure a student can be added to the university - Karsten"""
    def test_add_student(self):
        uni = University("UConn", [], [])
        student = uni.add_student("Karsten", 1)
        self.assertEqual(uni.get_student(1), student)

    """Checks that adding the same course twice does not create a duplicate - Karsten"""
    def test_duplicate_course(self):
        uni = University("UConn", [], [])
        course1 = uni.add_course("CSE1010", 3)
        course2 = uni.add_course("CSE1010", 3)
        self.assertEqual(course1, course2)

    """Makes sure None is returned if a student ID does not exist - Karsten"""
    def test_student_not_found(self):
        uni = University("UConn", [], [])
        self.assertIsNone(uni.get_student(99999))

    """Checks that course_enrollment returns the correct student names - Karsten"""
    def test_course_enrollment(self):
        uni = University("UConn", [], [])
        course = uni.add_course("CSE1010", 3)
        student = uni.add_student("Karsten", 1)
        course.add_student(student)

        names = uni.course_enrollment("CSE1010")
        self.assertEqual(names[0], "Karsten")

    """Checks that the correct number of students are returned for a course - Karsten"""
    def test_students_in_course(self):
        uni = University("UConn", [], [])
        course = uni.add_course("CSE1010", 3)
        student1 = uni.add_student("Karsten", 1)
        student2 = uni.add_student("Jaden", 2)

        course.add_student(student1)
        course.add_student(student2)

        students = uni.get_students_in_course("CSE1010")
        self.assertEqual(len(students), 2)


if __name__ == "__main__":
    unittest.main()
