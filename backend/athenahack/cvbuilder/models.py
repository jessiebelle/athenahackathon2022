from django.db import models

from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.ForeignKey
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Company(models.Model):
    id = models.BigAutoField()