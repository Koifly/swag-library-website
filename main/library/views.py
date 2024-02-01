import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def get_list_type(request):
    path = request.path
    list_type = os.path.basename(os.path.normpath(path))
    return list_type

def home(request):
    return render(request, "home.html")

def login(request):
	return render(request, "login.html")

def list(request):
	template = loader.get_template('list.html')

	list_type = get_list_type(request)
	title = list_type.capitalize()
	context = {
	'title' : title
	}
	return HttpResponse(template.render(context, request))