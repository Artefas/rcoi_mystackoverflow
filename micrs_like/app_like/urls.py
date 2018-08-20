from django.urls import path

from .views import LikeQuestionCreateAPIView, LikeAnswerListCreateAPIView
from .views import LikeQuestionRetrieveAPIView

urlpatterns = [
    path("like/question", LikeQuestionCreateAPIView.as_view(), name='create-like-for-question'),
    path("like/question/<int:question_id>/user/<int:user_id>", LikeQuestionRetrieveAPIView.as_view(), name='check-user-like-for-question'),
    path("like/answer", LikeAnswerListCreateAPIView.as_view(), name='create-or-check-user-like-for-answer'),
]