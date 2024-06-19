from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    age = models.IntegerField()
    address = models.TextField(max_length=200)
    date = models.DateField()
    image = models.ImageField(upload_to='media',null=True,blank=True)

