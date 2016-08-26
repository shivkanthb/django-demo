from django.contrib import messages
from django.core.mail import send_mail
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect

from django.http import HttpResponse
from django.shortcuts import render

from . import forms


def hello_world(request):
	# return HttpResponse('Hello, World!')
	return render(request,'home.html')


def suggestion_view(request):
	form = forms.SuggestionForm()
	if request.method == 'POST':
		form = forms.SuggestionForm(request.POST)
		if form.is_valid():
			print(request.POST)

	return render(request,'suggestion_form.html',{'form':form})