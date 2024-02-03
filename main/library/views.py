import os
from .contexts import context_dict
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

def build_context(request):
    list_type = get_list_type(request)

    context = context_dict[list_type]

    return context

@login_required(login_url="/login/")
def list(request):
    template = loader.get_template('list.html')
    context = build_context(request)
    
    return HttpResponse(template.render(context, request))