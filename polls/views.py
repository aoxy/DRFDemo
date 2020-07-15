from django.shortcuts import render
from django.shortcuts import get_object_or_404
# Create your views here.

from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Question, Choice
from .serializers import QuestionSerializer, ChoiceSerializer, VoteSerializer
from rest_framework import generics


def index(request):
    return HttpResponse("你好世界。你在投票目录首页。")


# class QuestionList(APIView):
#     def get(self, requset):
#         questions = Question.objects.all()[:20]
#         data = QuestionSerializer(questions, many=True).data
#         return Response(data)


# class QuestionDetail(APIView):
#     def get(self, request, pk):
#         question = get_object_or_404(Question, pk=pk)
#         data = QuestionSerializer(question).data
#         return Response(data)

class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


# class ChoiceList(generics.ListCreateAPIView):
#     queryset = Choice.objects.all()
#     serializer_class = ChoiceSerializer


# class CreateVote(generics.CreateAPIView):
#     serializer_class = VoteSerializer

class ChoiceList(generics.ListCreateAPIView):
    def get_queryset(self):
        queryset = Choice.objects.filter(question_id=self.kwargs['pk'])
        return queryset
    serializer_class = ChoiceSerializer


class CreateVote(APIView):
    serializer_class = VoteSerializer

    def post(self, request, pk, choice_pk):
        voted_by = request.data.get('voted_by')
        data = {'choice': choice_pk, 'question': pk, 'voted_by': voted_by}
        serializer = VoteSerializer(data=data)
        if serializer.is_valid():
            vote = serializer.save()
            print('成功')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('失败')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

