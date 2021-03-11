from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Chat, Message
from django.http import Http404



def index(request):
    template = loader.get_template('easymessage/index.html')
    
    all_chats = Chat.objects.all()
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'online_user':current_user,
        'all_chats': all_chats,
    }
    return HttpResponse(template.render(context, request))

def login(request):
    if request.POST:
        email = request.POST['email']
        password = request.POST['password']
        all_users = User.objects.all()
        for user in all_users:
            if user.login == email and password == user.password:
                request.session['user_id'] = user.id
                return redirect(index)

    return render(request, 'easymessage/login.html')

def chat_details(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    
    template = loader.get_template('easymessage/message.html')
    messages = Message.objects.filter(chat_id=chat_id).all()
    current_user = User.objects.get(id=request.session['user_id'])
    context = {
        'online_user':current_user,
        'messages': messages,
        'chat':chat
    }
    return HttpResponse(template.render(context, request))


def check_password(request, chat_id):
    chat = Chat.objects.get(id=chat_id)
    if request.POST.get('password'):
        password = request.POST['password']
        if password == chat.message_password:
            template = loader.get_template('easymessage/message.html')
            messages = Message.objects.filter(chat_id=chat_id).all()
            current_user = User.objects.get(id=request.session['user_id'])
            context = {
                'online_user':current_user,
                'messages': messages,
                'chat':chat
            }
            return HttpResponse(template.render(context, request))
    
        return redirect(index)

def save_message(request):
    if request.POST:
        text = request.POST['text']
        chat_id = request.POST['chat_id']
        chat = Chat.objects.get(pk=chat_id)
        user_id = request.session['user_id']
        user = User.objects.get(pk=user_id)
        obj = Message.objects.create(chat_id = chat, user_id = user, message_text = text)

        return redirect(chat_details, chat_id = chat_id)
