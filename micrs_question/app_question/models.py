from django.db import models

# Create your models here.

class Question(models.Model):
    question_id = models.IntegerField(primary_key=True)
    title       = models.CharField(max_length=128)
    text        = models.CharField(max_length=1024)
    pub_date    = models.DateField(auto_now_add=True)
    user_id     = models.IntegerField()

class Answer(models.Model):
    answer_id   = models.IntegerField(primary_key=True)
    question    = models.ForeignKey('Question', on_delete=models.CASCADE)
    text        = models.CharField(max_length=1024)
    marked      = models.BooleanField(default=False)
    pub_date    = models.DateField(auto_now_add=True)
    user_id     = models.IntegerField()

class CommentQuestion(models.Model):
    comment_id  = models.AutoField(primary_key=True)
    question    = models.ForeignKey('Question', on_delete=models.CASCADE)
    user_id     = models.IntegerField()
    text        = models.CharField(max_length=128)
    pub_date    = models.DateField(auto_now_add=True)

class CommentAnswer(models.Model):
    comment_id  = models.AutoField(primary_key=True)
    answer      = models.ForeignKey('Answer', on_delete=models.CASCADE)
    user_id     = models.IntegerField()
    text        = models.CharField(max_length=128)
    pub_date    = models.DateField(auto_now_add=True)

class VoteQuestion(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE,"Не нравится"),
        (LIKE, "Нравится")
    )

    vote_id     = models.AutoField(primary_key=True)
    user_id     = models.IntegerField()
    vote        = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    question    = models.ForeignKey('Question', on_delete=models.CASCADE)
    pub_date    = models.DateField(auto_now=True,auto_now_add=True)

class VoteAnswer(models.Model):
    LIKE = 1
    DISLIKE = -1

    VOTES = (
        (DISLIKE,"Не нравится"),
        (LIKE, "Нравится")
    )

    vote_id     = models.AutoField(primary_key=True)
    user_id     = models.IntegerField()
    vote        = models.SmallIntegerField(verbose_name="Голос", choices=VOTES)
    answer      = models.ForeignKey('Answer', on_delete=models.CASCADE)
    pub_date    = models.DateField(auto_now=True,auto_now_add=True)

class ModeratorTable(models.Model):
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    user_id     = models.IntegerField()






