from rest_framework import serializers

class QuestionSerializer(serializers.Serializer):
    question_id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=128)
    text = models.CharField(max_length=1024)
    pub_date = models.DateField(auto_now_add=True)
    user_id = models.IntegerField()
