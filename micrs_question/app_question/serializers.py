from rest_framework import serializers

from .models import Question, Answer, VoteQuestion, VoteAnswer, CommentQuestion, CommentAnswer

class QuestionWithVotesSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField()

    class Meta:
        model = Question
        fields = ('question_id','title','text','pub_date','user_id', 'votes')

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('question_id','title', 'text', 'pub_date','user_id')

class AnswerWithVotesSerializer(serializers.ModelSerializer):
    votes = serializers.IntegerField()

    class Meta:
        model = Answer
        fields = ('answer_id', 'text', 'marked', 'pub_date', 'user_id', 'votes')

class AnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Answer
        fields = ('answer_id', 'text', 'marked', 'pub_date', 'user_id')

class VoteQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoteQuestion
        fields = ('user_id', 'vote', 'question')

class VoteAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = VoteAnswer
        fields = ('user_id', 'vote', 'answer')

class CommentQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentQuestion
        fields = ('comment_id', 'question', 'user_id', 'text', 'pub_date')

class CommentAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CommentAnswer
        fields = ('comment_id', 'question', 'user_id', 'text', 'pub_date')