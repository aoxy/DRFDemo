from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import index, QuestionViewSet, ChoiceList, CreateVote, UserCreate

# urlpatterns = [
#     path('', index, name='index'),
#     path('questions/', QuestionList.as_view(), name='questions_list'),
#     path('questions/<int:pk>/', QuestionDetail.as_view(), name='questions_detail'),
#     path('choices/', ChoiceList.as_view(), name="choice_list"),
#     path('vote/', CreateVote.as_view(), name="create_vote"),
# ]
router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')

urlpatterns = [
    path('index/', index, name='index'),
    path('', include(router.urls)),
    path('questions/<int:pk>/choices/', ChoiceList.as_view(), name="choice_list"),
    path('questions/<int:pk>/choices/<int:choice_pk>/vote/',
         CreateVote.as_view(), name="create_vote"),
    path('users/', UserCreate.as_view(), name="user_create")
]
