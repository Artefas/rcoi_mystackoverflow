from django.http import HttpResponse
from django.views.decorators.http import require_http_methods

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Question, Answer, Comment, Tag
from .serializers import QuestionDetailSerializer, QuestionSerializer
from .serializers import AnswerSerializer
from .serializers import CommentSerializer
from .serializers import TagSerializer

# # вопросы
class QuestionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionDetailAPIView(generics.RetrieveAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionDetailSerializer

# # ответы
class AnswerCreateAPIView(generics.CreateAPIView):
    serializer_class = AnswerSerializer
    queryset = Answer.objects.all()

class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class TagListAPIView(generics.ListAPIView):
    serializer_class = TagSerializer

    def get_queryset(self):
        tags = Tag.objects.all()
        query_params = self.request.query_params.dict()
        for param in query_params:
            if param == "name":
                value = query_params["name"]
                if not isinstance(value, list):
                    tags = tags.filter(name__contains=value)
        return tags

class QuestionListByTagAPIView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        name = self.kwargs["name"]
        return Question.objects.filter(tags__name=name)

@require_http_methods(["PATCH",])
def like_question(request, pk):
    question = Question.likes.like(object_id=pk)
    if question is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )

@require_http_methods(["PATCH",])
def unlike_question(request, pk):
    question = Question.likes.unlike(object_id=pk)
    if question is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )

@require_http_methods(["PATCH",])
def like_answer(request, pk):
    answer = Answer.likes.like(object_id=pk)
    if answer is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )

@require_http_methods(["PATCH",])
def unlike_answer(request, pk):
    answer = Answer.likes.unlike(object_id=pk)
    if answer is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )

@require_http_methods(["PATCH",])
def mark_answer(request, pk):
    answer = Answer.objects.mark(object_id=pk)
    if answer is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )

@require_http_methods(["PATCH",])
def unmark_answer(request, pk):
    answer = Answer.objects.unmark(object_id=pk)
    if answer is None:
        return HttpResponse(
            content_type='application/json',
            status=404
        )
    return HttpResponse(
        content_type='application/json',
        status=200
    )









