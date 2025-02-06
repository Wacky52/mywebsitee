from django.http import HttpResponse
from django.shortcuts import render

from course.models import Course, Subject, Tutor
from home.models import Setting


# Create your views here.
def index(request):
    setting = Setting.objects.get()
    course = Course.objects.all()
    course_cr = Course.objects.all().order_by('id')[:4]
    subject_cr = Subject.objects.all().order_by('id')[:3]
    tutor_cr = Tutor.objects.all().order_by('id')[:3]
    page = 'home'
    context = {'setting': setting,
               'page': page,
               'subjects_cr': subject_cr,
               'course_cr': course_cr,
               'course': course,
               'tutor_cr': tutor_cr
               }
    return render(request,'index.html', context)


def about(request):
    # return HttpResponse("Hello Django!")
    setting = Setting.objects.get()
    context = {'setting': setting}
    return HttpResponse(request,'about.html', context)

def contact(request):
    # return HttpResponse("Hello Django!")
    setting = Setting.objects.get()
    context = {'setting': setting}
    return HttpResponse(request,'contact.html')