from rest_framework import generics
from rest_framework.pagination import PageNumberPagination

from .models import Tag, Question
from .serializers import TagSerializer, QuestionSerializer, QuestionInputSerializer

# Create your views here.

class TagView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = PageNumberPagination

class QuestionDetailView(generics.RetrieveDestroyAPIView):
    lookup_field = "question_id"

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionCreateView(generics.CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionInputSerializer


class QuestionByIdsView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        questions_id = self.request.query_params.getlist('question_id')
        return Question.objects.filter(question_id__in=questions_id)

class QuestionsListByTagViev(generics.ListAPIView):
    serializer_class = QuestionSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        tag_id = self.kwargs['tag_id']
        return Question.objects.filter(tags__tag_id=tag_id)


