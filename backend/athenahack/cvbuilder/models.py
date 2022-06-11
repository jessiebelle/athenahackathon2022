from django.db import models

class Language(models.Model):
    id = models.IntegerField(primary_key=True)
    language = models.CharField(max_length=2)


class Company(models.Model):
    name = models.CharField(max_length=100)

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    preferred_language = models.ForeignKey(Language, on_delete=models.CASCADE)

class AboutMe(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    about_me = models.CharField(max_length=2000, null=True)
    about_me_language_id = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)

class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)

class Experience(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    role_name = models.CharField(max_length=200)
    details = models.CharField(max_length=2000, null=True)

class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    skill_name = models.CharField(max_length=200)

class UserSkill(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)

class SkillDisplayName(models.Model):
    id = models.IntegerField(primary_key=True)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=200)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)

class UserLanguage(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)


class CV(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
