from django.shortcuts import render
from django.http import HttpResponse
import requests

# Create your views here.
def index(request):
	# return HttpResponse("Hello")
	context = ""
	return render(request, "skymav/index.html", context)