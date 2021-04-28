from rest_framework import viewsets
from polls.models import Question
from polls.serializers import QuestionSerializer
from polls.tasks import Polls


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.order_by('-pub_date')
    serializer_class = QuestionSerializer
