from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.conf import settings

# Create your models here.

#a class to define a table to save the poll questions in them
class Poll(models.Model):
    # the question it self with max 2000 char
    question = models.CharField(max_length=2000)

    # the user that created this poll
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # the date where this poll was created
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.question

#a class to define a table to save the responces and the questions themselves in them
class Choice(models.Model):
    # a ForeignKey to the poll table that this answers are for
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)

    #the text of the answer it self
    choice_text = models.CharField(max_length=200)

    #the number of people who chose this answer
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class User(AbstractUser):

    email_verify = models.BooleanField(default=False)

    def __str__(self):
        return self.username