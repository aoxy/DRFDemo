from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Question, Choice
from .serializers import QuestionSerializer


def index(request):
    return HttpResponse("你好世界。你在投票目录首页。")


class QuestionList(APIView):
    def get(self, requset):
        questions = Question.objects.all()[:20]
        data = QuestionSerializer(questions, many=True).data
        return Response(data)


class QuestionDetail(APIView):
    def get(self, request, pk):
        question = get_object_or_404(Question, pk=pk)
        data = QuestionSerializer(question).data
        return Response(data)
