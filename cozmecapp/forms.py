from django import forms
from .models import CourseModel, Testimonial, TeamMembers, Partners, Blog, Service, OfferEnquiry, Event, Gallery, EventRegistration


class CourseForm(forms.ModelForm):
    class Meta:
        model = CourseModel
        fields = '__all__'
        
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'designation', 'rating', 'message', 'image']
        
class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamMembers
        fields = '__all__'
 
 
class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = '__all__' 
        
class PartnersForm(forms.ModelForm):
    class Meta:
        model = Partners
        fields = '__all__'
 
        
class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = '__all__'
        
        
class ServiceForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = '__all__'
        
        
class OfferEnquiryForm(forms.ModelForm):
    class Meta:
        model = OfferEnquiry
        fields = '__all__'
        
    
class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'
        
class EventRegistrationForm(forms.ModelForm):
    class Meta:
        model = EventRegistration
        fields = '__all__'