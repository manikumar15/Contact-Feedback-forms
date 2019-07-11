from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .models import FeedbackData,ContactData,CoursesData
from .forms import FeedbackForm,ContactForm
import datetime
date1 = datetime.datetime.now()


def base(request):
    return render(request, 'base.html')

def home(request):
    return render(request, 'home.html')
    

def courses(request):
    courses=CoursesData.objects.all()
    return render(request,'courses.html',{'courses':courses})


def ourgallery(request):
    return render(request, 'ourgallery.html')

def team(request):
    return render(request, 'team.html')



def contact(request):
    if request.method == "POST":
        cform=ContactForm(request.POST)
        if cform.is_valid():
            name=cform.cleaned_data.get('name')
            email=cform.cleaned_data.get('email')
            mobile=cform.cleaned_data.get('mobile')
            courses=cform.cleaned_data.get('courses')
            shift=cform.cleaned_data.get('shift')
            location=cform.cleaned_data.get('location')
            gender=cform.cleaned_data.get('gender')
            date=cform.cleaned_data.get('date')

            data=ContactData(
                name=name,
                email=email,
                mobile=mobile,
                courses=courses,
                shift=shift,
                location=location,
                gender=gender,
                date=date
            )
            data.save()
            cform=ContactForm()
            return render(request, 'contact.html',{'cform':cform})
        else:
            return HttpResponse("Inavlid user data")
    else:
        cform=ContactForm()
        return render(request, 'contact.html',{'cform':cform})






def feedback(request):
    if request.method == "POST":
        fform=FeedbackForm(request.POST)
        if fform.is_valid():
            name=request.POST.get('name')
            rating=request.POST.get('rating')
            feedback=request.POST.get('feedback')

            data=FeedbackData(
                name=name,
                rating=rating,
                feedback=feedback,
                date=date1
                )
            data.save()
            fform=FeedbackForm()
            fdata = FeedbackData.objects.all()
            return render(request,'feedback.html',{'fform': fform,'fdata': fdata})
        
        else:
            return HttpResponse('Invalid User Data')
    else:
        fform = FeedbackForm()
        fdata = FeedbackData.objects.all()
        return render(request,'feedback.html',{'fform': fform,'fdata': fdata})



def register(request):
    return render(request, 'register.html')


def index(request):
    return render(request, 'index.html')





