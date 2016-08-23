from django.test import TestCase

from django.utils import timezone

# Create your tests here.

from .models import Course

class CourseModelTests(TestCase):
	def test_course_creation(self):
		course = Course.objects.create(
			title="test title 1",description="test title description"
		)
		now = timezone.now()
		self.assertLess(course.created_at,now)
