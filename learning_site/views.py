from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def hello_world(request):
	# return HttpResponse('Hello, World!')
	return render(request,'home.html')


def suggestion_view(request):
	form = forms.SuggestionForm()
	return render(request,'suggestion_form.html',{'form':form})