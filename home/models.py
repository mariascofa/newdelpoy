import django_filters
from django.db import models
from django.contrib.postgres.fields import JSONField



class Student(models.Model):
    """This data consists of various
    fields with information about students."""

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    normalized_name = models.CharField(max_length=200, null=True)
    age = models.IntegerField(null=True)
    sex = models.CharField(max_length=200, null=True)
    address = models.CharField(max_length=200, null=True)
    description = models.TextField(null=True)
    birthday = models.DateField('Birthday (d/m/Y)', null=True)
    email = models.CharField(max_length=200, null=True)
    social_url = models.CharField(max_length=200, null=True)
    book = models.OneToOneField('home.Book', on_delete=models.CASCADE, null=True, related_name="student")
    subject = models.ForeignKey('home.Subject', on_delete=models.SET_NULL, null=True, related_name="student")




class Subject(models.Model):
    title = models.CharField(max_length=200)

class Book (models.Model) :
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)

class Teacher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    students = models.ManyToManyField('home.Student', related_name="teacher")

class Currency(models.Model):
    ccy = models.CharField(max_length=200)
    base = models.CharField(max_length=200)
    buy = models.CharField(max_length=200)
    sale = models.CharField(max_length=200)





