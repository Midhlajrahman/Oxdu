from __future__ import unicode_literals

import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404,render

from .forms import ContactForm, RegisterationForm, RegisterForm
from .models import (Course, CourseFeatures, Event, EventPoints, Faq,
                     OurFacualty, Testimonial)

def index(request):
    form = ContactForm(request.POST or None)
    courses = Course.objects.all()
    events = Event.objects.all()  # Fetch all events from the database

    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
            return HttpResponse(
                json.dumps(response_data), content_type="application/javascript"
            )
    else:
        facualty = OurFacualty.objects.all()
        testimonial = Testimonial.objects.all()
        context = {"facualty": facualty, "testimonial": testimonial, "courses": courses, "events": events}
        return render(request, "web/index.html", context)


def about(request):
    testimonial = Testimonial.objects.all
    context = {"testimonial": testimonial}
    return render(request, "web/about.html", context)


def blog(request):
    return render(request, "web/blog.html")


def category(request):
    return render(request, "web/category.html")


def coming_soon(request):
    return render(request, "web/coming-soon.html")


def contact(request):
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        context = {
            "is_contact": True,
            "form": form,
        }
    return render(request, "web/contact.html", context)


def error(request):
    return render(request, "web/error.html")


def faq(request):
    faq = Faq.objects.all()
    context = {"faq": faq}
    return render(request, "web/faq.html", context)


def portfolio(request):
    return render(request, "web/portfolio-details.html")


def pricing(request):
    return render(request, "web/pricing.html")


def privacy(request):
    return render(request, "web/privacy.html")


def authentication(request):
    return render(request, "web/profile-authentication.html")


def service_details(request):
    return render(request, "web/service-details.html")


def service(request):
    return render(request, "web/services.html")


def team(request):
    facualty = OurFacualty.objects.all()
    context = {"facualty": facualty}
    return render(request, "web/team.html", context)


def events(request):
    event = Event.objects.all()
    context = {"event": event}
    return render(request, "web/events.html", context)


def event_details(request, pk):
    event = get_object_or_404(Event, pk=pk)
    event_points = EventPoints.objects.filter(event=event)
    form = RegisterForm(request.POST or None)
    if request.method == "POST":
        print(request.POST) 

        if form.is_valid():
            registration = form.save(commit=False)
            registration.event = event
            registration.save()

            response_data = {
                "status": "true",
                "title": "Successfully Registered",
                "message": "Your Seat successfully Secured",
            }
            return JsonResponse(response_data)
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
            return JsonResponse(response_data)
    else:
       
        other_events = Event.objects.exclude(pk=pk)
        context = {
            "event": event,
            "form": form,
            "other_events": other_events,
            "event_points": event_points,
        }

    return render(request, "web/event-details.html", context)


def course(request):
    courses = Course.objects.all()
    context = {
        "courses": courses,
    }

    return render(request, "web/course.html", context)


def course_details(request, pk):
    # Get the selected course
    course = get_object_or_404(Course, pk=pk)
    # Get features for the selected course
    features = CourseFeatures.objects.filter(course=course)
    # Get other courses (excluding the selected one)
    other_courses = Course.objects.exclude(pk=pk)
    form = RegisterationForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            # Save the form data to the database
            registration = form.save(commit=False)
            registration.course = course
            registration.save()

            response_data = {
                "status": "true",
                "title": "Successfully Registered",
                "message": "Your Seat successfully Secured",
            }
            return HttpResponse(
                json.dumps(response_data), content_type="application/javascript"
            )
        else:
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
            }
            return HttpResponse(
                json.dumps(response_data), content_type="application/javascript"
            )

    context = {
        "course": course,
        "form": form,
        "features": features,
        "other_courses": other_courses,  # Add this to your context
    }

    return render(request, "web/course-details.html", context)
