from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    # return HttpResponse("Hello Django!")
    return render(request,'index.html')


def about(request):
    # return HttpResponse("Hello Django!")
    return HttpResponse(request,'about.html')
def contact(request):
    # return HttpResponse("Hello Django!")
    return HttpResponse(request,'contact.html')