from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from msrest import Serializer
from .models import Question
from rest_framework import viewsets
from .serializers import QuestionSerializers

class ViewApi(viewsets.ModelViewSet):
    queryset=Question.objects.all()
    serializer_class=QuestionSerializers

def index(request):
    latest_question_list=Question.objects.order_by('-pub_date')
    #output='\t'.join([q.question_text for q in latest_question_list])
    context={
        'latest_question_list':latest_question_list
    }
    return render(request,'polls/index.html',context)
    
def detail(request,question_id):
    question=get_object_or_404(Question,pk=question_id)
    context={
       'question':question 
    }
    return render(request,'polls/detail.html',context)

def results(request,question_id):
    return HttpResponse("You are looking at results of question %s" %question_id)

def vote(request,question_id):
    return HttpResponse("You are voting on question %s" %question_id)
    