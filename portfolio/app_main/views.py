from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse,reverse_lazy

#import from app_main models
from app_main.models import Home,About,Portfolio
# Create your views here.
def index(request):
    home=Home.objects.latest('updated')
    about=About.objects.latest('updated')
    portfolio=Portfolio.objects.all()
    diction={'title':'welcome to tonmoyPlanet','home':home,'about':about,'profiles':portfolio}
    return render(request,'app_main/index.html',context=diction)