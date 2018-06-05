from django.db import models

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=32)
    description = models.CharField(max_length=256)


class QuestionTagsManager(models.Manager):
    def get_tags_by_question_id(self, question_id):
        return super().get_queryset().filter(question_id=question_id)

    def get_tagged_questions(self, tag_title):
        return super().get_queryset().filter(tag_title=tag_title)


class QuestionTags(models):
    question_id = models.IntegerField()
    tag = models.ForeignKey('Tag', on_delete=models.CASCADE)
    objects = QuestionTagsManager()

    class Meta:
        unique_together = ('question_id', 'tag')

