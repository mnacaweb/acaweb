from django.test import TestCase

from acamar_api.manager import AcamarCourseManager, AcamarPositionManager


class CourseTest(TestCase):
    def test_connection(self):
        result = AcamarCourseManager.all(cached=False)
        self.assertIsInstance(result, list)

    def test_content_length(self):
        result = AcamarCourseManager.all(cached=False)
        self.assertGreater(len(result), 0)


class PositionTest(TestCase):
    def test_connection(self):
        result = AcamarPositionManager.get_data("cs", False)
        self.assertIsInstance(result, dict)