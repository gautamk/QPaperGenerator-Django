from django.db import models

# Create your models here.
class Department(models.Model):
    name = models.CharField(max_length = 200)
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField( null = True , blank = True)
    
    def __unicode__(self):
        return self.name

class Subject(models.Model):
    subject_code = models.CharField(max_length = 200 , null = True , blank = True)
    name = models.CharField(max_length = 200)
    department = models.ForeignKey('Department')
    added_at = models.DateTimeField(auto_now=True)
    description = models.TextField(null = True , blank = True)
    
    def __unicode__(self):
        return self.name

class Question(models.Model):
    subject = models.ForeignKey('Subject')
    question = models.TextField()
    question_types = (
        ('A' , 'Part A'),
        ('B' , 'Part B'),
        )
    question_type = models.CharField(max_length = 20 , choices = question_types)
    unit_number = models.PositiveSmallIntegerField(null = True , blank = True)
    comments = models.TextField( null = True , blank = True)
    added_at = models.DateTimeField(auto_now=True)
    
    def __unicode__(self):
        return self.question
    
    
    