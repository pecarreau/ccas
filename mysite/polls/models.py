from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
    
class Aides(models.Model):
    name = models.CharField(max_length = 200, unique = False)
    price = models.IntegerField(max_length = 15, unique = False, blank = True)
    
class Recipients(models.Model):
    id = models.CharField(max_length = 200, primary_key = True)
    name = models.CharField(max_length = 200, unique = False)
    surname = models.CharField(maxlength = 200, unique = False)
    birthday = models.DateField()
    email = models.EmailField(max_length = 254)
    allowed_social_support = models.ManyToManyField(Aides)
    possessed_social_support = models.ManyToManyField(Aides)
    needed_social_support = models.ManyToManyField(Aides)
    def __str__(self):
        return self.id
    
class Simulations(models.Model):
    date = models.DateField()
    recipient = models.ForeignKey(Recipients, on_delete = models.CASCADE)
    list_of_support = models.ExpressionList()
