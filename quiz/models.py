from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.
typechoics = (
    ('1', 'Active'),
    ('0', 'InActive')
)
class quiz(models.Model):
    name=models.CharField(unique=True,max_length=100)
    status=models.CharField(
        max_length = 20,
        choices = typechoics,
        default = '0'
        )
    def __str__(self):
        return self.name

class question(models.Model):
    quiz=models.ForeignKey(quiz,on_delete=models.CASCADE)
    question=models.CharField(max_length=400)
    option1=models.CharField(max_length=100)
    option2=models.CharField(max_length=100)
    option3=models.CharField(max_length=100)
    option4=models.CharField(max_length=100)
    answer=models.CharField(max_length=100)

    def __str__(self):
        return self.question



class useranswers(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    quiz = models.ForeignKey(quiz, on_delete=models.CASCADE)
    q1=models.CharField(max_length=200,null=True)
    q2 = models.CharField(max_length=200,null=True)
    q3 = models.CharField(max_length=200,null=True)
    q4 = models.CharField(max_length=200,null=True)
    q5 = models.CharField(max_length=200,null=True)
    q6 = models.CharField(max_length=200,null=True)
    q7 = models.CharField(max_length=200,null=True)
    q8 = models.CharField(max_length=200,null=True)
    q9 = models.CharField(max_length=200,null=True)
    q10 = models.CharField(max_length=200,null=True)

class userinfo(models.Model):
    userid=models.ManyToManyField(User)
    question=models.ManyToManyField(useranswers)
    date=models.DateTimeField(auto_now=datetime.date)
    result = models.IntegerField(null=True)
