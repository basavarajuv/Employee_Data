from django.shortcuts import render
from .forms import EmpForm
from .models import EmpData
from django.http import HttpResponse
# Create your views here.

def Movie_view(request):
    if request.method == "POST":
        pass
    else:
        cform = EmpForm()
        return render(request, 'Emp.html', {'ffrom': cform})