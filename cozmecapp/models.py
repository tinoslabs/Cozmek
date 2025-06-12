from django.db import models

# Create your models here.


class CourseModel(models.Model): 
    course_name = models.CharField(max_length=100)
    title = models.CharField(max_length=100,null=True, blank=True) 
    image = models.ImageField(upload_to='course_images/')   
    level = models.CharField(max_length=100,null=True, blank=True)
    student_count = models.PositiveIntegerField(default=0, null=True, blank=True)  # Number of students enrolled
    lessons = models.PositiveIntegerField(default=0, null=True, blank=True)  # Number of lessons in the course    
    language = models.CharField(max_length=100,null=True, blank=True)  # Language of instruction
    course_fee = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Course fee
    rating = models.PositiveSmallIntegerField(default=5,null=True, blank=True)  # 1 to 5 stars
    duration_months = models.PositiveIntegerField(help_text="Duration in months",null=True, blank=True)
    total_classes = models.PositiveIntegerField(null=True, blank=True) 
    certification = models.CharField(max_length=500, null=True,blank=True)       
    coaching_details = models.TextField(null=True, blank=True)
    course_brochure = models.FileField(upload_to='course_brochures/', null=True, blank=True) 
    course_video = models.FileField(upload_to='course_videos/', null=True, blank=True)
    upcoming_batch = models.DateField(null=True, blank=True)  # Date of the next batch
    seats_available = models.PositiveIntegerField(default=0, null=True, blank=True)  # Number of seats available in the course
    def __str__(self):
        return self.course_name
    
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    rating = models.PositiveSmallIntegerField(default=5)  # 1 to 5 stars
    message = models.TextField()
    image = models.ImageField(upload_to='testimonial_images/')

    def __str__(self):
        return f"{self.name} - {self.designation}"
    
    
class TeamMembers(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    image = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    
    
class Partners(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    logo = models.ImageField(upload_to='team_images/')

    def __str__(self):
        return self.name
    
    
class Blog(models.Model):
    blog_heading = models.CharField(max_length=100)
    blog_details = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
    date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return self.blog_heading
    
    
class Service(models.Model):
    heading = models.CharField(max_length=100)
    details = models.TextField(null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
   
    def __str__(self):
        return self.heading
    
    
class OfferEnquiry(models.Model):
    name = models.CharField(max_length=100)   
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True) 
      
    def __str__(self):
        return self.name
 
 
class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery_images/')    
    def __str__(self):
        return f"Gallery Image {self.id}"    

    
class EventRegistration(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=12, blank=True, null=True)
   
    event = models.ForeignKey('Event', on_delete=models.CASCADE, related_name='registrations')
    
    def __str__(self):
        return self.name
 
    
class Event(models.Model):
    
    event_heading = models.CharField(max_length=100)
    event_details = models.TextField(null=True, blank=True)
    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    venue = models.CharField(max_length=255, null=True, blank=True)
    main_image = models.ImageField(upload_to='images/')
    location = models.CharField(max_length=500, null=True, blank=True)
          
    def __str__(self):
        return self.event_heading