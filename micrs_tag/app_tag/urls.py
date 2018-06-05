from django.urls import path

from .views import TagView, QuestionTagsView

urlpatterns = [
    path('tags', TagView.as_view(), name='tags-list'),
    path('question/<int:question_id>', QuestionTagsView.as_view() , name='question-tags-list'),
    path('question/tagged/<str:title>', , name='questions-tagged-list'),
]