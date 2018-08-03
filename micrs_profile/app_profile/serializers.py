from rest_framework import serializers

from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user_id', 'about', 'url_facebook', 'url_vk','url_twitter','url_github','rating','registration_date']

