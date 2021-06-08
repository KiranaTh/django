from django.db import models

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=300)
    fullname = models.CharField(max_length=300)
    birthDate = models.CharField(max_length=300)
    age = models.CharField(max_length=300)
    education = models.CharField(max_length=300)
    university = models.CharField(max_length=300)
    workplace = models.CharField(max_length=300)
    position = models.CharField(max_length=300)
    pic_url = models.CharField(max_length=300)
    facebook_url = models.CharField(max_length=300)
    instragram_url = models.CharField(max_length=300)
    github_url = models.CharField(max_length=300)

class Email(models.Model):
    email = models.CharField(max_length=300)
    

