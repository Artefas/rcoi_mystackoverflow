from django.shortcuts import render

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from django.db.models import Count

from .models import Question, Answer, VoteQuestion, VoteAnswer
from .serializers import QuestionSerializer, QuestionWithVotesSerializer
from .serializers import AnswerSerializer, AnswerWithVotesSerializer
from .serializers import VoteQuestionSerializer, VoteAnswerSerializer

# вопросы
class QuestionWithVotesListView(generics.ListAPIView):
    queryset = Question.objects.annotate(votes = Count('votequestion'))
    serializer_class = QuestionWithVotesSerializer
    pagination_class = PageNumberPagination

class QuestionWithVotesDetailView(generics.RetrieveAPIView):
    queryset = Question.objects.annotate(votes=Count('votequestion'))
    serializer_class = QuestionWithVotesSerializer
    lookup_field = 'question_id'

class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailView(generics.UpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    lookup_field = 'question_id'

# ответы
class AnswerWithVotesListByQuestionIdView(generics.ListAPIView):
    serializer_class = AnswerWithVotesSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        question_id = self.kwargs["question_id"]
        answers = Answer.objects.filter(question__question_id = question_id).annotate(votes=Count('voteanswer'))
        return answers


class AnswerWithVotesDetailView(generics.RetrieveAPIView):
    queryset = Answer.objects.annotate(votes=Count('voteanswer'))
    serializer_class = AnswerWithVotesSerializer


class AnswerCreateView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    pagination_class = PageNumberPagination


class AnswerDetailView(generics.UpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

# голоса за вопросы
class VoteQuestionCreateView(generics.CreateAPIView):
    queryset = VoteQuestion.objects.all()
    serializer_class = VoteQuestionSerializer

class VoteQuestionUpdateView(generics.UpdateAPIView):
    queryset = VoteQuestion.object.all()
    serializer_class = VoteQuestionSerializer

# голоса за ответы
class VoteAnswerCreateView(generics.CreateAPIView):
    queryset = VoteAnswer.objects.all()
    serializer_class = VoteAnswerSerializer

class VoteAnswerUpdateView(generics.UpdateAPIView):
    queryset = VoteAnswer.objects.all()
    serializer_class = VoteAnswerSerializer





