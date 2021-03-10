# Generated by Django 3.1.7 on 2021-03-10 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_password', models.CharField(max_length=50)),
                ('last_message', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=70)),
                ('age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_text', models.CharField(max_length=400)),
                ('sent_date', models.DateTimeField(auto_now_add=True)),
                ('chat_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='easymessage1.chat')),
            ],
        ),
        migrations.AddField(
            model_name='chat',
            name='opponent_user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_opponent_user_id', to='easymessage1.user'),
        ),
        migrations.AddField(
            model_name='chat',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_user_id', to='easymessage1.user'),
        ),
    ]