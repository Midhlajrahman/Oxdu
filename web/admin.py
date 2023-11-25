from django.contrib import admin
from .models import Contact, Course, CourseFeatures, OurFacualty , Event , Faq , Testimonial ,Register , CourseRegistration


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")

class CourseFeaturesInline(admin.TabularInline):
    model = CourseFeatures
    fields = ('course_feature',)  # Corrected the fields attribute
    extra = 1


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("full_name" , "email" , "contact_number" , "location")


@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name","email","phone")

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name', "course_description" , "duration" , "fees" , )  # Corrected the list_display attribute
    inlines = [CourseFeaturesInline]


@admin.register(OurFacualty)
class OurFacualtyAdmin(admin.ModelAdmin):
    list_display =( "facualty_name" , "facualty_position" , "facualty_image" , "instagram" , "linkedin" , "twitter")
    

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ("event_title" , "location" , "event_cordinator" , "event_month" , "event_date" , "event_image" , "event_description" , "event_points")
    
    
@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("faq_question" , "faq_answer")
    

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (  "name" , "testimonial_content"  , "position")
    