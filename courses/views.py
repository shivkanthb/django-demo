from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.
from .models import Course

def course_list(request):
	c = Course.objects.all()
	# output = ', '.join([str(course) for course in c])
	# return HttpResponse(output)
	return render(request,'courses/course_list.html',{'courses':c})

def course_detail(request,pk):
	# course = Course.objects.get(pk=pk)
	course = get_object_or_404(Course,pk=pk)
	return render(request,'courses/course_detail.html',{'course':course})