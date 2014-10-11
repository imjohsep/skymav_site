from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms

import requests

# Contact Form 
class NameForm(forms.Form):
	your_name = forms.CharField(label='Your name', max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Your name'}))
	your_email = forms.EmailField(label='Your email', widget=forms.TextInput(attrs={'placeholder': 'Your name'}))

# Create your views here.
def index(request):
	# return HttpResponse("Hello")
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data['your_name']
			email = form.cleaned_data['your_email']
			response = mailgun(name, email)
			if response == 'successful':
				return HttpResponseRedirect('')
			else:
				return HttpResponseRedirect('500.html')
	else:
		form = NameForm()
	return render(request, 'skymav/index.html', {'form': form})

# def index(request):
# 	# return HttpResponse("Hello")
# 	context = ""
# 	return render(request, "skymav/index.html", context)

def get_name(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = NameForm()
	return render(request, 'skymav/name.html', {'form': form})

def mailgun(name, email):
	sandbox = 'sandbox42328ec0591e42889705c371101ef799.mailgun.org'
	recipient = 'imjohsep@gmail.com'
	request_url = 'https://api.mailgun.net/v2/{0}/messages'.format(sandbox)
	request = requests.post(request_url,
		auth=("api", 'key-d7f3a1a915b59dc2eec0290e983dfe25'),
		data={"from": recipient,
			  "to": recipient,
			  "subject": "I'm Interested!",
			  "text": name+" "+email})

	# context = 'Status: {0}'.format(request.status_code)
	# context += ' Body:   {0}'.format(request.text)
	# 'Body:   {0}'.format(request.text)

	return 'successful'
	# return HttpResponse()

def contact(request):
	if request.method == 'POST':
		form = NameForm(request.POST)
		if form.is_valid():
			return HttpResponseRedirect('')
	else:
		form = NameForm()
	return render(request, 'skymav/contact.html', {'form': form})

def documentation(request):
	context = ''
	return render(request, 'skymav/documentation.html', context)
	