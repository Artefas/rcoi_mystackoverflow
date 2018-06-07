from django.urls import path

from .views import QuestionCreateView,QuestionDetailView
from .views import QuestionWithVotesDetailView, QuestionWithVotesListView
from .views import AnswerCreateView, AnswerDetailView
from .views import AnswerWithVotesDetailView, AnswerWithVotesListByQuestionIdView
from .views import V

urlpatterns = [
    path('questions',                   QuestionWithVotesListView.as_view(), name='questions-with-votes-list'),
    path('questions/<int:question_id>', QuestionWithVotesDetailView.as_view(), name='questions-with-votes-detail'),
    path('questions/new',               QuestionCreateView.as_view(), name='question-create'),
    path('questions/<int:question_id>/detail',  QuestionDetailView.as_view(), name='question-detail'),
    path('questions/<int:question_id>/answers', AnswerWithVotesListByQuestionIdView.as_view(), name='answer-with-votes-list-by-question-id'),
    path('answer',                      AnswerCreateView.as_view(), name='answer-create'),
    path('answer/<int:answer_id>',      AnswerDetailView.as_view(), name='answer-detail'),
    path('questions/<int:question_id>/vote', ),
    path('answer/<int:answer_id>/vote', )
]