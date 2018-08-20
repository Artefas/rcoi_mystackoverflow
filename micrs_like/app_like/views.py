from rest_framework import generics
from rest_framework.generics import get_object_or_404

from .models import Like
from .serializers import LikeQuestionSerializer, LikeAnswerSerializer
# Create your views here.

class LikeQuestionCreateAPIView(generics.CreateAPIView):
    serializer_class = LikeQuestionSerializer
    queryset = Like.objects.all()

class LikeQuestionRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LikeQuestionSerializer
    queryset = Like.objects.filter(object_type="Q")

    def get_object(self):
        queryset = self.queryset
        filter = {
            "user_id": self.kwargs["user_id"],
            "object_id": self.kwargs["question_id"]
        }
        liked_question = get_object_or_404(queryset, **filter)
        return liked_question

class LikeAnswerListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = LikeAnswerSerializer

    def get_queryset(self):
        params = self.request.query_params
        user_id = params.get("user_id", None)
        answers_id = params.getlist("answer_id", None)

        answers = Like.objects.filter(user_id=user_id, object_id__in=answers_id, object_type="A")
        return answers
