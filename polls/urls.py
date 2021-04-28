from django.urls import include, path
from rest_framework import routers
from polls.views import QuestionViewSet

router = routers.DefaultRouter()
router.register(r'questions', QuestionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
