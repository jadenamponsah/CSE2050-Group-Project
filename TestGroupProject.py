import unittest
from GroupProject import Course, Student, University


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
