from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()

    def __str__(self) :
        return self.title

class Score(models.Model):
    school = models.CharField(max_length=20)
    name = models.CharField(max_length=20)
    string = models.CharField(max_length=20)
    integer = models.IntegerField()

    def __str__(self) :
        return self.name
    
