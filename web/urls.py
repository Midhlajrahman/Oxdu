"""
URL configuration for oxdu project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("blog/", views.blog, name="blog"),
    path("event-details/<str:pk>/", views.event_details, name="event-details"),
    path("category/", views.category, name="category"),
    path("coming-soon", views.coming_soon, name="coming-soon"),
    path("contact", views.contact, name="contact"),
    path("error", views.error, name="error"),
    path("faq", views.faq, name="faq"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("events", views.events, name="events"),
    path("pricing", views.pricing, name="pricing"),
    path("privacy", views.privacy, name="privacy"),
    path("authentication", views.authentication, name="authentication"),
    path("service-details", views.service_details, name="service-details"),
    path("service", views.service, name="service"),
    path("team", views.team, name="team"),
    path("course", views.course, name="course"),
    path("course_details/<str:pk>/", views.course_details, name="course_details"),
]
