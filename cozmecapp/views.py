
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect

from .models import  CourseModel, Testimonial, TeamMembers, Partners, Blog, Service, OfferEnquiry
from .forms import  CourseForm, TestimonialForm, TeamForm, PartnersForm, BlogForm, ServiceForm, OfferEnquiryForm
# Create your views here.
from django.contrib import messages

from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse 
import os


def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.error(request, "There was an error logging in, try again...")
            return redirect('user_login')
    return render(request, 'authenticate/login.html', {'form': True})

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "You were logged out")
    return redirect('index')


def index(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
       
        OfferEnquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
           
        )
        messages.success(request, "Thank you! Your message has been submitted.")
        return redirect('index')
    course = CourseModel.objects.all().order_by('-id')
    instructor = TeamMembers.objects.all().order_by('-id')
    testimonial = Testimonial.objects.all().order_by('-id')
    blog = Blog.objects.all().order_by('-id')
    partners = Partners.objects.all().order_by('-id')
    return render(request,'index.html',{'course':course,'instructor':instructor, 'testimonial':testimonial,'blog':blog,'partners':partners})


def admin_dashboard(request):
    return render(request,'admin_pages/admin_dashboard.html')


@csrf_exempt
def ckeditor_upload(request):
    if request.method == 'POST' and request.FILES.get('upload'):
        upload = request.FILES['upload']
        file_extension = os.path.splitext(upload.name)[1].lower()
        
        # Check if the uploaded file is an image or a PDF
        if file_extension in ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']:
            folder = 'images'
        elif file_extension == '.pdf':
            folder = 'pdfs'
        else:
            return JsonResponse({'uploaded': False, 'error': 'Unsupported file type.'})

        # Save the file in the appropriate folder
        file_name = default_storage.save(f'{folder}/{upload.name}', ContentFile(upload.read()))
        file_url = default_storage.url(file_name)
        return JsonResponse({
            'uploaded': True,
            'url': file_url
        })
    
    return JsonResponse({'uploaded': False, 'error': 'No file was uploaded.'})


@login_required(login_url='user_login')
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_course') 
    else:
        form = CourseForm()

    return render(request, 'admin_pages/add_course.html', {'form': form})

@login_required(login_url='user_login')
def view_course(request):
    course = CourseModel.objects.all().order_by('-id')
    return render(request, 'admin_pages/view_course.html', {'course': course})

@login_required(login_url='user_login')
def update_course(request, id):
    course = get_object_or_404(CourseModel, id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            return redirect('view_course')
    else:
        form = CourseForm(instance=course)
    return render(request, 'admin_pages/update_course.html', {'form': form, 'course': course})

@login_required(login_url='user_login')
def delete_course(request,id):
    coaching = CourseModel.objects.get(id=id)
    coaching.delete()
    return redirect('view_course')

@login_required(login_url='user_login')
def add_testimonial(request):
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list_testimonials')
    else:
        form = TestimonialForm()
    return render(request, 'admin_pages/add_testimonial.html', {'form': form})


@login_required(login_url='user_login')
def list_testimonials(request):
    testimonials = Testimonial.objects.all()
    return render(request, 'admin_pages/list_testimonials.html', {'testimonials': testimonials})

@login_required(login_url='user_login')
def update_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    if request.method == 'POST':
        form = TestimonialForm(request.POST, request.FILES, instance=testimonial)
        if form.is_valid():
            form.save()
            return redirect('list_testimonials')
    else:
        form = TestimonialForm(instance=testimonial)
    return render(request, 'admin_pages/update_testimonial.html', {'form': form})

@login_required(login_url='user_login')
def delete_testimonial(request, pk):
    testimonial = get_object_or_404(Testimonial, pk=pk)
    testimonial.delete()
    return redirect('list_testimonials')


@login_required(login_url='user_login')
def add_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_team') 
    else:
        form = TeamForm()

    return render(request, 'admin_pages/add_team.html', {'form': form})

@login_required(login_url='user_login')
def view_team(request):
    team = TeamMembers.objects.all().order_by('-id')
    return render(request,'admin_pages/view_team.html',{'team':team})


@login_required(login_url='user_login')
def update_team(request,id):
    team = get_object_or_404(TeamMembers, id=id)
    if request.method == 'POST':
        form = TeamForm(request.POST, request.FILES, instance=team)
        if form.is_valid():
            form.save()
            return redirect('view_team')
    else:
        form = TeamForm(instance=team)
    return render(request, 'admin_pages/update_team.html', {'form': form, 'team': team})


@login_required(login_url='user_login')
def delete_team(request,id):
    team = TeamMembers.objects.get(id=id)
    team.delete()
    return redirect('view_team')

@login_required(login_url='user_login')
def add_partners(request):
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_partners') 
    else:
        form = PartnersForm()

    return render(request, 'admin_pages/add_partners.html', {'form': form})


@login_required(login_url='user_login')
def view_partners(request):
    logo = Partners.objects.all().order_by('-id')
    return render(request,'admin_pages/view_partners.html',{'logo':logo})


@login_required(login_url='user_login')
def update_partners(request,id):
    logos = get_object_or_404(Partners, id=id)
    if request.method == 'POST':
        form = PartnersForm(request.POST, request.FILES, instance=logos)
        if form.is_valid():
            form.save()
            return redirect('view_partners')
    else:
        form = PartnersForm(instance=logos)
    return render(request, 'admin_pages/update_partners.html', {'form': form, 'logos': logos})


@login_required(login_url='user_login')
def delete_partners(request,id):
    logos = Partners.objects.get(id=id)
    logos.delete()
    return redirect('view_partners')


@login_required(login_url='user_login')
def add_blog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_blog') 
    else:
        form = BlogForm()

    return render(request, 'admin_pages/add_blog.html', {'form': form})

@login_required(login_url='user_login')
def view_blog(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request,'admin_pages/view_blog.html',{'blog':blog})

@login_required(login_url='user_login')
def update_blog(request, id):
    blog = get_object_or_404(Blog, id=id)  # <-- Was TeamMembers
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            return redirect('view_blog')
    else:
        form = BlogForm(instance=blog)
    return render(request, 'admin_pages/update_blog.html', {'form': form, 'blog': blog})

@login_required(login_url='user_login')
def delete_blog(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    return redirect('view_blog')

@login_required(login_url='user_login')
def add_service(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('view_service') 
    else:
        form = ServiceForm()

    return render(request, 'admin_pages/add_service.html', {'form': form})

@login_required(login_url='user_login')
def view_service(request):
    service = Service.objects.all().order_by('-id')
    return render(request,'admin_pages/view_service.html',{'service':service})

@login_required(login_url='user_login')
def update_service(request, id):
    service = get_object_or_404(Service, id=id)
    if request.method == 'POST':
        form = ServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            return redirect('view_service')
    else:
        form = ServiceForm(instance=service)  # <-- fixed from instance=blog

    return render(request, 'admin_pages/update_service.html', {'form': form, 'service': service})

@login_required(login_url='user_login')
def delete_service(request,id):
    service = Service.objects.get(id=id)
    service.delete()
    return redirect('view_service')


@login_required(login_url='user_login')
def view_enquiries(request):
    enquiry = OfferEnquiry.objects.all().order_by('-id')
    return render(request,'admin_pages/view_enquiries.html',{'enquiry':enquiry})


@login_required(login_url='user_login')
def delete_enquiry(request,id):
    enquiry = OfferEnquiry.objects.get(id=id)
    enquiry.delete()
    return redirect('view_enquiries')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')


def blog(request):
    blog = Blog.objects.all().order_by('-id')
    return render(request,'blog.html',{'blog':blog})


def courses(request):
    courses = CourseModel.objects.all().order_by('-id')
    return render(request,'courses.html',{'courses':courses})


def instructors(request):
    instructors = TeamMembers.objects.all().order_by('-id')
    return render(request,'instructor.html',{'instructors':instructors})


def blog_details(request, id):
    blog = get_object_or_404(Blog, id=id)
    return render(request, 'blog-details.html', {'blog': blog})


def course_details(request, id):
    course = get_object_or_404(CourseModel, id=id)
    return render(request,'courses_details.html', {'course': course})


