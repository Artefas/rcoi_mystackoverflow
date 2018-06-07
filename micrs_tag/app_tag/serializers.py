from rest_framework import serializers

from .models import Tag, Question

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag_id', 'title', 'description')

class QuestionSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ('question_id', 'tags')

class QuestionInputSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True, read_only=False, queryset=Tag.objects.all())

    class Meta:
        model = Question
        fields = ('question_id', 'tags')

