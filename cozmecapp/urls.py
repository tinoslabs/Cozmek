from django.urls import path
from . import views
from ckeditor_uploader import views as ckeditor_views

urlpatterns = [
    
    path('',views.index,name='index'),
    path('user_login', views.user_login, name='user_login'),
    path('logout_user', views.logout_user, name='logout_user'),
    
    path('admin_dashboard', views.admin_dashboard, name='admin_dashboard'),
    path('ckeditor_upload/', views.ckeditor_upload, name='ckeditor_upload'),
    
    path('add_course', views.add_course, name='add_course'),
    path('view_course', views.view_course, name='view_course'),
    path('delete_course/<int:id>', views.delete_course, name='delete_course'),
    path('update_course/<int:id>', views.update_course, name='update_course'),
    
    path('add_testimonial', views.add_testimonial, name='add_testimonial'),
    path('list_testimonials', views.list_testimonials, name='list_testimonials'),
    path('update_testimonial/<int:pk>/', views.update_testimonial, name='update_testimonial'),
    path('delete_testimonial/<int:pk>/', views.delete_testimonial, name='delete_testimonial'),
     
    path('add_team', views.add_team, name='add_team'),
    path('view_team', views.view_team, name='view_team'),   
    path('update_team/<int:id>/', views.update_team, name='update_team'),
    path('delete_team/<int:id>/', views.delete_team, name='delete_team'),
    
    path('add_partners', views.add_partners, name='add_partners'),
    path('view_partners', views.view_partners, name='view_partners'),   
    path('update_partners/<int:id>/', views.update_partners, name='update_partners'),
    path('delete_partners/<int:id>/', views.delete_partners, name='delete_partners'),
    
    path('add_blog', views.add_blog, name='add_blog'),
    path('view_blog', views.view_blog, name='view_blog'),
    path('update_blog/<int:id>/', views.update_blog, name='update_blog'),
    path('delete_blog/<int:id>/', views.delete_blog, name='delete_blog'),
    
    path('add_service', views.add_service, name='add_service'),
    path('view_service', views.view_service, name='view_service'),
    path('update_service/<int:id>/', views.update_service, name='update_service'),
    path('delete_service/<int:id>/', views.delete_service, name='delete_service'),
    
    path('add_event', views.add_event, name='add_event'),
    path('view_event', views.view_event, name='view_event'),
    path('update_event/<int:id>/', views.update_event, name='update_event'),
    path('delete_event/<int:id>/', views.delete_event, name='delete_event'),
      
    path('view_enquiries', views.view_enquiries, name='view_enquiries'),
    path('delete_enquiry/<int:id>/', views.delete_enquiry, name='delete_enquiry'),
    
    
    path('add_gallery', views.add_gallery, name='add_gallery'),
    path('view_gallery', views.view_gallery, name='view_gallery'),
    path('update_gallery/<int:id>/', views.update_gallery, name='update_gallery'),
    path('delete_gallery/<int:id>/', views.delete_gallery, name='delete_gallery'),
    
    
    
    path('events', views.events, name='events'),
    path('event_details/<int:id>/', views.event_details, name='event_details'),
    
    path('gallery', views.gallery, name='gallery'),
    
    path('services',views.services,name='services'),
    path('service_details/<int:service_id>/',views.service_details,name='service_details'),
    
    path('registration_list', views.registration_list, name='registration_list'),
    path('delete_list/<int:id>/', views.delete_list, name='delete_list'),
     
    path('ckeditor/upload/', ckeditor_views.upload, name='ckeditor_upload'),
    path('ckeditor/browse/', ckeditor_views.browse, name='ckeditor_browse'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),
    path('blog',views.blog,name='blog'),
    path('courses',views.courses,name='courses'),
    path('instructors',views.instructors,name='instructors'),
    path('blog_details/<int:id>/',views.blog_details,name='blog_details'),
    path('course_details/<int:id>/', views.course_details, name='course_details')
]