from django.db import models

# Create your models here.

class Tag(models.Model):
    tag_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    tags = models.ManyToManyField(Tag)

