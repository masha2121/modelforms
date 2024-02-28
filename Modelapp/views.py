from django.shortcuts import render
from Modelapp.forms import Studentsform

# Create your views here.
def index(request):
    stud=Studentsform
    return render(request,'index.html',{'form':stud})