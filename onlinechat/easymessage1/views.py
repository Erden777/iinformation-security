from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User
from django.http import Http404


def index(request):
    template = loader.get_template('easymessage/login.html')
    all_users = User.objects.all()
    context = {
        'users': all_users,
    }
    return HttpResponse(template.render(context, request))

def chat_details(request, chat_id):
    return HttpResponse("You're looking at question %s." % chat_id)

def login(request):
    
    return HttpResponse("hello")