from django.urls import path

from .views import TagView, QuestionDetailView, QuestionByIdsView, QuestionCreateView, QuestionsListByTagViev

urlpatterns = [
    path('tags', TagView.as_view(), name='tags-list'),
    path('question/<int:question_id>', QuestionDetailView.as_view() , name='question-tags-list'),
    path('questions', QuestionByIdsView.as_view() , name='questions-tags-by-ids'),
    path('question', QuestionCreateView.as_view() , name='question-tags-create'),
    path('questions/tagged/<int:tag_id>', QuestionsListByTagViev.as_view() , name='question-tags-list-by-tag'),
]