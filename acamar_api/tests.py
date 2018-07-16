from django.test import TestCase

from acamar_api.manager import AcamarCourseManager


class CourseTest(TestCase):
    def test_connection(self):
        result = AcamarCourseManager.all(cached=False)
        self.assertIsInstance(result, list)

    def test_content_length(self):
        result = AcamarCourseManager.all(cached=False)
        self.assertGreater(len(result), 0)
