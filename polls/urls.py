from django.urls import path

from .views import index, QuestionList, QuestionDetail

urlpatterns = [
    path('', index, name='index'),
    path('questions/', QuestionList.as_view(), name='questions_list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='questions_detail')
]
