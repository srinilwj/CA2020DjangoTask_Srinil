from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, "index.html")

def second_index(request):
    return HttpResponse("Welcome to the custom url page of Learning-Django!")