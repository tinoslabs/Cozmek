from django.urls import path
from . import views
# from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('courses',views.courses,name='courses'),
    path('instructors',views.instructors,name='instructors'),
    path('blog_details',views.blog_details,name='blog_details'),
    path('courses_details',views.courses_details,name='courses_details'),
]