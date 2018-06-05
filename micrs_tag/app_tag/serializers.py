from rest_framework import serializers

from .models import Tag, QuestionTags

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id', 'title', 'description', 'count',)

class QuestionTagsSerializer(serializers.ModelSerializer):
    tags = serializers.TagSerializer(many=True, read_only=True)

    class Meta:
        model = QuestionTags
        fields = ('id', 'question_id', 'tags')


class QuestionTagsInputSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(many=True)

    class Meta:
        model = QuestionTags
        fields = ('id', 'question_id', 'tags')