from django.db import models

class User(models.Model):
    full_name = models.CharField(max_length=70)
    age = models.IntegerField()
    login = models.CharField(max_length=40)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.full_name



class Chat(models.Model):
    message_password = models.CharField(max_length=50)
    last_message = models.CharField(max_length=200)
    user_id = models.ForeignKey(User, related_name='related_user_id', on_delete=models.CASCADE)
    opponent_user_id = models.ForeignKey(User, related_name='related_opponent_user_id', on_delete=models.CASCADE)

    def __str__(self):
        return last_message

class Message(models.Model):
    chat_id = models.ForeignKey(Chat, on_delete=models.CASCADE)
    message_text = models.CharField(max_length=400)
    sent_date = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.headline