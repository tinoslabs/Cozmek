
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

# from .models import  Contact, Testimonial, Partners, TeamMembers, Blog, Service
# from .forms import  ContactForm, TestimonialForm, PartnersForm, TeamForm, BlogForm, ServiceForm
# Create your views here.
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse 
import os



def index(request):
    return render(request,'index.html')



def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def blog(request):
    return render(request,'blog-grid.html')


def courses(request):
    return render(request,'courses-2.html')


def instructors(request):
    return render(request,'instructors-carousel-2.html')


def blog_details(request):
    return render(request,'blog-details.html')


def courses_details(request):
    return render(request,'courses_details.html')
