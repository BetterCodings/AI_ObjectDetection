from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(default='media/default_image.jpg')

class User(models.Model):
    name= models.CharField(max_length=30)
    ID =models.CharField(max_length=30,primary_key=True)
    Passwd=models.CharField(max_length=30)
    def login():

        return 

class Lecture(models.Model):
    ID = models.CharField(max_length=30,primary_key=True)
    subject = models.CharField(max_length=30)
    pID = models.ForeignKey(User,on_delete=models.CASCADE)
    sum = models.IntegerField(default=0)

class Class(models.Model):
    day = models.CharField(max_length=30)
    preiod = models.CharField(max_length=30)
    ID =models.ForeignKey(Lecture,on_delete=models.CASCADE)
    classroom=models.CharField(max_length=30)
    class Meta:
        constraints= [models.UniqueConstraint(fields=["day","preiod","ID"],name="Class-unique")]

class Attendence(models.Model):
    date=models.DateTimeField('date published')
    ID =models.ForeignKey(Lecture,on_delete=models.CASCADE)
    attend=models.IntegerField(default=0)
    image = models.ImageField(default='media/default_image.jpg')
    class Meta:
        constraints= [models.UniqueConstraint(fields=["date","ID"],name="Attendence-unique")]