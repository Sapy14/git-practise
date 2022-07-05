from .models import Question
from rest_framework import serializers

class QuestionSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Question
        fields=("id","url","question_text","pub_date")