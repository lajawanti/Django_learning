from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
      # return HttpResponse("<h1 style = 'color: red'>Hello....<h1>")
      return render(request, 'basic.html', {'title' : 'Django'})

def profile(request):
      return HttpResponse("My profile page....")