from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=70)
    age = models.IntegerField()
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name



class Chat(models.Model):
    title = models.CharField(max_length=50)
    message_password = models.CharField(max_length=50)

    def __str__(self):
        return self.title
        
class ChatinUsers(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, related_name='related_user_id', on_delete=models.CASCADE)
    subscribed_date = models.DateTimeField(auto_now_add=True, blank=True)

class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=400)
    sent_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    user_id = models.ForeignKey(User, related_name='related_sended_user_id', on_delete=models.CASCADE)

    def __str__(self):
        return self.message_text