from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers

from .models import Like

class LikeQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def validate_object_type(self, value):
        if not isinstance(value, str) or value != "Q":
            raise serializers.ValidationError("Ожидалось значение 'Q'")
        return value

    def create(self, validated_data):
        try:
            like = Like.objects.get(
                user_id = validated_data["user_id"],
                object_id=validated_data["object_id"],
                object_type=validated_data["object_type"]
            )
            like.user_like = validated_data["user_like"]
        except ObjectDoesNotExist:
            like = Like(**validated_data)
        like.save()
        return like


class LikeAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = '__all__'

    def validate_object_type(self, value):
        if not isinstance(value, str) or value != "A":
            raise serializers.ValidationError("Ожидалось значение 'A'")
        return value

    def create(self, validated_data):
        try:
            like = Like.objects.get(
                user_id = validated_data["user_id"],
                object_id=validated_data["object_id"],
                object_type=validated_data["object_type"]
            )
            like.user_like = validated_data["user_like"]
        except ObjectDoesNotExist:
            like = Like(**validated_data)
        like.save()
        return like



