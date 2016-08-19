from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Course

def course_list(request):
	c = Course.objects.all()
	# output = ', '.join([str(course) for course in c])
	# return HttpResponse(output)
	return render(request,'courses/course_list.html',{'courses':c})