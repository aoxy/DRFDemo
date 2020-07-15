from django.urls import path

from .views import index, QuestionList, QuestionDetail, ChoiceList, CreateVote

urlpatterns = [
    path('', index, name='index'),
    path('questions/', QuestionList.as_view(), name='questions_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='questions_detail'),
    path('choices/', ChoiceList.as_view(), name="choice_list"),
    path('vote/', CreateVote.as_view(), name="create_vote"),
]
