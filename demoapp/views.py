from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from .models import Place
from .models import Team
def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request,"index.html",{'result':obj,'team':obj1})