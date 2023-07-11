from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.

def Display_Student_Form(request):
    SFO = StudentForm()
    d = {'SFO': SFO}
    if request.method == 'POST':
        SFD = StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse('DATA IS VALID')
        else:
            return HttpResponse('DATA IS NOT VALID')
    return render(request,'Display_Student_Form.html',d)