from django.db import models

# Create your models here.

# model names must be singular by convention

class Course(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=100)
	description = models.TextField()


	def __str__(self):
		return self.title

class Step(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField()
	order = models.IntegerField(default=0)
	course = models.ForeignKey(Course)

	def __str__(self):
		return self.title;