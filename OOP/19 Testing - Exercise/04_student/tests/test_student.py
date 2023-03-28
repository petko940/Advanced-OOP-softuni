import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self) -> None:
        self.student = Student("Petko",
                               {"course_name": ["note1", "note2"]})

    def test_init(self):
        self.assertEqual(self.student.name, "Petko")
        self.assertEqual(self.student.courses, {"course_name": ["note1", "note2"]})

    def test_enroll_if_course_name_in_courses(self):
        result = self.student.enroll("course_name", ["note2"])
        self.assertEqual(result, "Course already added. Notes have been updated.")
        self.assertEqual(self.student.courses["course_name"][1], "note2")

    def test_enroll_if_course_name_is_(self):
        self.student.courses["Petko"] = []
        result = self.student.enroll("math", ["math notes"])
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(self.student.courses["math"][0], "math notes")

    def test_enroll_last(self):
        self.student.courses["Petko"] = []
        result = self.student.enroll("math", ["math notes"], "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertEqual(self.student.courses["math"][0], "math notes")

    def test_add_new_course_without_adding_the_notes(self):
        self.student.courses["Petko"] = []
        result = self.student.enroll("math", ["math notes"], "N")
        self.assertEqual(len(self.student.courses["math"]), 0)
        self.assertEqual("Course has been added.", result)

    def test_add_notes_is_course_name_in_courses(self):
        result = self.student.add_notes("course_name", ["something"])
        self.assertEqual(result, "Notes have been updated")

    def test_add_notes_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("missing_course", "something")
        self.assertEqual(str(ex.exception), "Cannot add notes. Course not found.")

    def test_leave_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("no name")
        self.assertEqual(str(ex.exception), "Cannot remove course. Course not found.")

    def test_leave_course(self):
        self.student.enroll("course_name_2", ["note1"], "")
        result = self.student.leave_course("course_name_2")
        self.assertEqual(result, "Course has been removed")


if __name__ == '__main__':
    unittest.main()
