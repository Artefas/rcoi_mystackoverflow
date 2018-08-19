from django.db import models
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType

class LikeManager(models.Manager):
    def like(self, object_id):
        try:
            obj = self.get_queryset().get(id=object_id)
            obj.votes += 1
            obj.save(update_fields=["votes",])
            return obj
        except ObjectDoesNotExist:
            return None

    def unlike(self, object_id):
        try:
            obj = self.get_queryset().get(id=object_id)
            obj.votes -= 1
            obj.save(update_fields=["votes",])
            return obj
        except ObjectDoesNotExist:
            return None

class AnswerManager(models.Manager):
    def mark(self, answer_id):
        try:
            answer = self.get_queryset().get(id=answer_id)
            answer.marked  = True
            answer.save(update_fields=["marked",])
            return answer
        except ObjectDoesNotExist:
            return None

    def unmark(self, answer_id):
        try:
            answer = self.get_queryset().get(id=answer_id)
            answer.marked  = False
            answer.save(update_fields=["marked",])
            return answer
        except ObjectDoesNotExist:
            return None

class Question(models.Model):
    title       = models.CharField(max_length=128)
    text        = models.CharField(max_length=1024)
    pub_date    = models.DateField(auto_now_add=True)
    user_id     = models.IntegerField()
    votes       = models.IntegerField(default=0)
    comments    = GenericRelation('Comment')
    tags        = models.ManyToManyField('Tag')

    objects = models.Manager()
    likes = LikeManager()

class Answer(models.Model):
    question    = models.ForeignKey('Question', related_name='answers', on_delete=models.CASCADE)
    text        = models.CharField(max_length=1024)
    marked      = models.BooleanField(default=False)
    pub_date    = models.DateField(auto_now_add=True)
    user_id     = models.IntegerField()
    votes       = models.IntegerField(default=0,blank=True)
    comments    = GenericRelation('Comment')

    likes = LikeManager()
    objects = AnswerManager()

class Comment(models.Model):
    id  = models.AutoField(primary_key=True)
    user_id     = models.IntegerField()
    text        = models.CharField(max_length=128)
    pub_date    = models.DateField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class Tag(models.Model):
    name = models.CharField(max_length=16)
    description = models.CharField(max_length=128, blank=True,default="")

    def __str__(self):
        return self.name






