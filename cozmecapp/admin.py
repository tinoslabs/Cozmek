from django.contrib import admin
from .models import CourseModel, Testimonial, TeamMembers, Partners, Blog, Service, OfferEnquiry
# Register your models here.
admin.site.register(CourseModel)
admin.site.register(Testimonial)        
admin.site.register(TeamMembers)
admin.site.register(Partners)
admin.site.register(Blog)
admin.site.register(Service)
admin.site.register(OfferEnquiry)