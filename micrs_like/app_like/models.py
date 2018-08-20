from django.db import models

# Create your models here.

class Like(models.Model):
    LIKE = 1
    DISLIKE = -1
    LIKE_STATUS_CHOICES = (
        (LIKE, "Нравится"),
        (DISLIKE, "Не нравится")
    )
    TYPE_OBJECT_CHOICES = (
        ("Q", "Вопрос"),
        ("A", "Ответ")
    )

    user_id = models.IntegerField(verbose_name="ID пользователя")
    object_type = models.CharField(verbose_name="Тип лайкнутого обекта", max_length=1, choices=TYPE_OBJECT_CHOICES)
    object_id = models.IntegerField(verbose_name="ID лайкнутого обекта")
    user_like = models.IntegerField(choices=LIKE_STATUS_CHOICES, default=LIKE)
    date_of_creation = models.DateTimeField(verbose_name="Дата создания",auto_created=True, auto_now=True)
    date_of_change = models.DateTimeField(verbose_name="Дата изменения решеняи", auto_now_add=True)


