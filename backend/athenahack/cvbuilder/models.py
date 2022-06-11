from django.db import models

from django.db import models

class Language(models.Model):
    language = models.CharField(max_length=200)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


class Company(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
