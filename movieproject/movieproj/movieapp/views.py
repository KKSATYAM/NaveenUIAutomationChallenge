from django.shortcuts import render
from movieapp.forms import StudentForm

# Create your views here.

def index_view(request):
    form=StudentForm()
    
    return render(request,"movieapp/index.html",{'form':form})



