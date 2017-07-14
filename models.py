from django.db import models
import os
import

from datetime import datetime

# Create your models here.


class User(models.Model):
    First_name = models.CharField(max_length=500)
    Last_name = models.CharField(max_length=500)
    DOB = models.DateField()
    Email_id = models.EmailField(max_length=254)
    Password = models.CharField(max_length=50)
    Place = models.CharField(max_length=100)
    Image =models.ImageField(upload_to=get_image_path,blank=True,null=true)
    user=models.Charfield(max_length=50)

    def get_image_path(instance, filename):
        return os.path.join('photos', str(instance.id), filename)

    def __str__(self):
        return "{}".format(self.user)

class category(models.Model):
    id = models.AutoField(primary_key=True)
    product_name=models.CharField(max_length=500)



    def __str__(self):
        return "{}.{}".format(self.id +"-"+ self.user)
class Question(models.Model):
    sub= models.CharField(max_length=500)
    question=models.TextField(max_length=5000)
    User_Id= models.ForeignKey(User)
    Product_id=models.ForeignKey(category)
    timestamp = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.sub

class Answer(models.Model):
    timestamp2=models.DateTimeField(auto_now_add=True)

    answer=models.TextField(max_length=5000)
    Ques_Id=models.ForeignKey(Question)
    User_id=models.ForeignKey(user)


    def __str__(self):
            return "{} | {} ".format(self.Ques_Id.User_Id.user,self.User_id.user)
class stats(models.Model):
    Ans_Id=models.ForeignKey(Answer)
    comments=models.TextField(max_length=5000)
    com_votes=models.IntegerField()
    timestamp3=models.DateTimeField(auto_now_add=True)
    U_Id=ForeignKey(User)

    def __str__(self):
        return "{}.{}".format(self.comments,self.com_votes)
class Vote(models.Model):
    Ans_Id= models.ForeignKey(Answer)
    User_Id=models.ForeignKey(User)
    UP/Down=models.CharField(max_length=5)

class QuestionView(models.Model):
    question = models.ForeignKey(Question, related_name='questionviews')
    ip = models.CharField(max_length=40)
    session = models.CharField(max_length=40)
    created = models.DateTimeField(default=datetime.datetime.now())
