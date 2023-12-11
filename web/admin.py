from django.contrib import admin

from .models import (Contact, Course, CourseFeatures, CourseRegistration,
                     Event, EventPoints, Faq, OurFacualty, Register,
                     Testimonial)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email")


class CourseFeaturesInline(admin.TabularInline):
    model = CourseFeatures
    fields = ("course_feature",) 
    extra = 1


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "course_name",
        "course_description",
        "duration",
        "fees",
    ) 
    inlines = [CourseFeaturesInline]


@admin.register(Register)
class RegisterAdmin(admin.ModelAdmin):
    list_display = ("full_name", "email", "contact_number", "location")


@admin.register(CourseRegistration)
class CourseRegistrationAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(OurFacualty)
class OurFacualtyAdmin(admin.ModelAdmin):
    list_display = (
        "facualty_name",
        "facualty_position",
        "facualty_image",
        "instagram",
        "linkedin",
        "twitter",
    )


class EventsPointsInline(admin.TabularInline):
    model = EventPoints
    fields = ("event_points",)  
    extra = 1


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = (
        "event_title",
        "location",
        "event_cordinator",
        "event_month",
        "event_date",
        "event_image",
        "event_description",
    )
    inlines = [EventsPointsInline]


@admin.register(Faq)
class FaqAdmin(admin.ModelAdmin):
    list_display = ("faq_question", "faq_answer")


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "testimonial_content", "position")
