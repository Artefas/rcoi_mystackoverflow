from django.urls import path

from .views import QuestionDetailAPIView, QuestionListCreateAPIView
from .views import AnswerCreateAPIView
from .views import CommentCreateAPIView
from .views import like_question, unlike_question
from .views import like_answer, unlike_answer
from .views import mark_answer, unmark_answer
from .views import TagListAPIView
from .views import QuestionListByTagAPIView

urlpatterns = [
    path('questions', QuestionListCreateAPIView.as_view(), name='questions-create-or-get-list'),
    path('questions/<int:pk>', QuestionDetailAPIView.as_view(), name='questions-detail'),
    path('comment', CommentCreateAPIView.as_view(), name='add-comment'),
    path('answer', AnswerCreateAPIView.as_view(), name='add-answer'),
    path('answer/<int:pk>/marked',      mark_answer, name='mark-answer'),
    path('answer/<int:pk>/unmarked',    unmark_answer, name='unmark-answer'),
    path('answer/<int:pk>/like',        like_answer, name='like-answer'),
    path('answer/<int:pk>/unlike',      unlike_answer, name='unlike-answer'),
    path('question/<int:pk>/like',      like_question, name='like-question'),
    path('question/<int:pk>/unlike',    unlike_question, name='unlike-question'),
    path('tags', TagListAPIView.as_view(), name='tags-list'),
    path('questions/tagged/<name>', QuestionListByTagAPIView.as_view(), name='questions-by-tag'),
]