from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist

from .models import Question, Answer, Comment, Tag
from .servises import get_comments


class CommentSerializerMixin(serializers.Serializer):
    comments = serializers.SerializerMethodField()

    def get_comments(self, obj):
        comments = get_comments(obj)
        return comments

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'

    def create(self, validated_data):
        try:
            tag = Tag.objects.get(name = validated_data["name"])
        except ObjectDoesNotExist:
            tag = Tag.objects.create(**validated_data)
        return tag

class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True)

    class Meta:
        model = Question
        fields = ('id','title','text','pub_date','user_id', 'votes', 'tags')

    def create(self, validated_data):
        tags = validated_data.pop('tags')
        question = Question.objects.create(**validated_data)

        for tag in tags:
            tag, created = Tag.objects.get_or_create(name=tag["name"])
            question.tags.add(tag)
        return question

class AnswerSerializer(serializers.ModelSerializer, CommentSerializerMixin):

    class Meta:
        model = Answer
        fields = ('id', 'text', 'marked', 'pub_date', 'user_id', 'votes', 'comments')

class QuestionDetailSerializer(serializers.ModelSerializer, CommentSerializerMixin):
    answers = AnswerSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('id','title', 'text', 'pub_date','user_id','answers','comments', 'tags')

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'