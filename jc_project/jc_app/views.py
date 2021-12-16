from django.shortcuts import render,redirect
from django.http import JsonResponse
import json
import datetime
from django.core import paginator
from django.core.paginator import Paginator

from .models import *


# Create your views here.

def home(request):
    carousel = Carousel.objects.all()
    context  = {
        'carousel' : carousel
    }
    return render(request, "jc_app/home.html", context)

def jobs(request):
    Jobs = job.objects.all()

#=================================== Search functionality of items ====================

    item_name = request.GET.get('item_name')
    if item_name !='' and item_name is not None:
        Jobs = Jobs.filter(JobTitle__icontains=item_name)
#=================================== Paginator code ====================
    paginator = Paginator(Jobs,2)
    page = request.GET.get('page')
    Jobs = paginator.get_page(page)

    return render(request,'jc_app/jobs.html',{'Jobs':Jobs})

def register(request):
    if request.method=='POST':
        name = request.POST['name']
        Emailid =  request.POST['emailid']
        phonenumber =  request.POST['phonenumber']
        qualification =  request.POST['qualification']
        Gender =  request.POST['Gender']
        yearofpassing =  request.POST['yearofpassing']
        HigherEducation =  request.POST['HigherEducation']
        place = request.POST['place']
        Resume =  request.POST['Resume']
        JobForm =jobform.objects.create(name=name,Emailid=Emailid,phonenumber=phonenumber,qualification=qualification,Gender=Gender,yearofpassing=yearofpassing,HigherEducation=HigherEducation,place=place,Resume=Resume)
        JobForm.save()
        return redirect('/')


    return render(request,'jc_app/register.html')

def contact(request):
    if request.method=='POST':
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        ContactUs = contactus.objects.create(firstName=firstName,lastName=lastName,email=email,mobile=mobile,message=message)
        ContactUs.save()
        return redirect('/')
    return render(request,'jc_app/contact.html')

def JobDetails(request,id):
    job_detail = job.objects.get(id=id)

    return render(request,'jc_app/jobdetails.html',{'job_detail':job_detail})


