# Generated by Django 3.1.7 on 2021-03-10 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easymessage1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='login',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
