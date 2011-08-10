# Create your views here.
from django.shortcuts import render_to_response , redirect
from QPaperGenerator.QP.forms import *
from QPaperGenerator.QP.models import *
from django.http import HttpRequest ,HttpResponse
def GenerateQuestionPaperGetDetails(request):
    if request.method == "GET":
        for Sub in Subject.objects.all():
            
    return HttpResponse(form)
