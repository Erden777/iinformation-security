from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import User, Chat, Message
from django.http import Http404

def egcd(e,r):
        while(r!=0):
            e ,r = r , e%r
        return e

def eea(a,b):
    if(a%b==0):
        return(b,0,1)
    else:
        gcd,s,t = eea(b,a%b)
        s = s-((a//b) * t)
        return(gcd,t,s)
    
def mult_inv(e,r):
    gcd,s,_=eea(e,r)
    
    if(gcd!=1):
        return None
    else:
        return s%r

def encrypt(public_key,n_text):
        
        e,n=public_key
        x=[]
        m=0
        for i in n_text:
            if(i.isupper()):
                m = ord(i)-65
                c=(m**e)%n
                x.append(c)
            elif(i.islower()):               
                m= ord(i)-97
                c=(m**e)%n
                x.append(c)
            elif(i.isspace()):
                spc=400
                x.append(400)
        
        return x

def decrypt(private_key,c_text):
        
        d,n=private_key
        txt=c_text.split(',')
        x=''
        m=0
        for i in txt:
            if(i=='400'):
                x+=' '
            else:
                m=(int(i)**d)%n
                m+=65
                c=chr(m)
                x+=c
        
        return x

def decryptpassword(password):
    p = 7
    q = 11
    n = p * q
    r= (p-1)*(q-1)
    
    for i in range(1,1000):
        if(egcd(i,r)==1):
            e=i
    
    d = mult_inv(e,r)
    public = (e,n)
    private = (d,n)
        
    message = password

    enc_msg=encrypt(public,message)

    print("Your encrypted message is:",enc_msg)

    return enc_msg


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
        attemps = request.session.get('attemps', '')
        email = request.POST['email']
        password = request.POST['password']
        all_users = User.objects.all()
        for user in all_users:
            password = decryptpassword(str(password))
            strpassword = ''
            for passo in password:
                strpassword += str(passo)
            if user.login == email and strpassword == user.password:
                request.session['user_id'] = user.id
                return redirect(index)
        if attemps is not '':
            print(attemps)
            if attemps >= 3 :
                request.session.set_expiry(10)
                request.session['banned'] = 1
                return render(request, 'easymessage/error.html')
        
    return redirect(singin)


def singin(request):
    if 'attemps' not in request.session :
        request.session['attemps'] = 0
    attemps = request.session['attemps']
    attemps +=1
    request.session['attemps'] = attemps
    if 'banned' in request.session:
        return render(request, 'easymessage/error.html')
    
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

        password = decryptpassword(password)
        strpassword = ''
        for passo in password:
            strpassword += str(passo)

        if strpassword == chat.message_password:
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

def register(request):
    if request.POST:
        full_name = request.POST.get('full_name', '')
        age = request.POST.get('age', 20)
        email = request.POST.get('email' ,'')
        password = request.POST.get('password', '')
        password = decryptpassword(password)
        strpassword = ''
        for passo in password:
            strpassword += str(passo)

        user = User.objects.create(full_name=full_name, age=age, login=email, password= strpassword)
        print(user)
        return redirect(login)
    return render(request, 'easymessage/register.html')