from rest_framework.serializers import HyperlinkedModelSerializer
from polls.models import Question


class QuestionSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ['id', 'question_text', 'pub_date']
