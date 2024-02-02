import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def home(request):
    return render(request, "home.html")


def get_list_type(request):
    path = request.path
    list_type = os.path.basename(os.path.normpath(path))
    return list_type

@login_required(login_url="/login/")
def list(request):
    template = loader.get_template('list.html')

    list_type = get_list_type(request)
    title = list_type.capitalize()
    context = {
    'title' : title
    }
    return HttpResponse(template.render(context, request))